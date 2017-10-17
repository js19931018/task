#coding=utf-8
import json
import re
import logging
import django_redis
import threading
import urlparse,urllib,json
import logging


from time import sleep,ctime
from django.http import HttpResponse
from logana.models import Logdata,Clientip
from exceptions import KeyError
from Queue import Queue

SCHEME = 'http'
NETLOCT = 'ip.taobao.com'
PATH = '/service/getIpInfo.php'
PARAMS = ''
FRAGMENT = ''
LIP = '10.10.251.212'


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

reqlist=[]
iddict={}
iddict_quick={}
get_ip_thread=[]
PRODUCENUM=100
THREAD_QUEUE=Queue(100)
QUERY_QUEUE=Queue(100)
check_thread=[]
countdict={}
page_dict={}
ip_region={}

class Query_Queue_Func(object):
    def __init__(self,func,args,name=''):
        self.queue=QUERY_QUEUE
        self.name=name
        self.func=func
        self.args=args
    def __call__(self):
        self.func(*self.args)


def produce(queue,inputlist):
    queue.put(inputlist)
    logger.info('read one pack')

def consume(queue,nloop):
    for i in range(nloop):
        l = queue.get()
        try:
            Logdata.objects.bulk_create(l)
            logger.info('saved pack %s'%i)
        except:
            logger.debug('save sql failed, num %s'%len(l))


def logrequest(request):
    if request.method == "POST":
        l = len(reqlist)
        if l <= 100:
            reqlist.append(l)
        else:
            return HttpResponse('busy')
        loglist=[]
        querylist=[]
        file_l = request.body
        print type(file_l)
        logger.info('start split %s'%ctime())
        lst = file_l.split('\n')
        logger.info('end split %s'%ctime())
        logger.debug('nums of log:%s' %len(lst))
        logger.info('start handle line %s' % ctime())
        for item in lst:
            alog = item.split()
            if not len(alog) == 14 :
                loglist.append(alog)
            else:
                l = Logdata(date=alog[0], time=alog[1], s_ip=alog[2], cs_method=alog[3], cs_uri_stem=alog[4], cs_uri_query=alog[5], s_port=alog[6], cs_username=alog[7], c_ip=alog[8], cs_user_agent=alog[9],sc_status=alog[10], sc_substatus=alog[11], sc_win32_status=alog[12], time_taken=alog[13], ip_region='unknown', ip_city='unknown')
                querylist.append(l)

        logger.info('end handle line %s' % ctime())
        Logdata.objects.bulk_create(querylist)
        t = threading.Thread(target=check_id())

        if not reqlist==[]:
            reqlist.pop()

        if loglist == []:
            return HttpResponse('OK')
        else:
            return HttpResponse(loglist)
        return HttpResponse('Get log successful %s \n%s'%(type(file), lst))
    else:
        return HttpResponse('need post method')

def logrequest_skethy(request):
    if request.method == "POST":
        l = len(reqlist)
        if l <= 100:
            reqlist.append(l)
        else:
            return HttpResponse('busy')
        loglist=[]
        querylist=[]
        iplist=[]
        file_l = request.body
        print type(file_l)
        logger.info('start split %s'%ctime())
        lst = file_l.split('\n')
        logger.info('end split %s'%ctime())
        logger.debug('nums of log:%s' %len(lst))
        logger.info('start handle line %s' % ctime())
        nloop = len(lst)//PRODUCENUM
        threading.Thread(target=(Query_Queue_Func(consume, (QUERY_QUEUE, nloop)))).start()
        for item in lst:
            alog = item.split()
            if not len(alog) == 14 :
                loglist.append(alog)
            else:
                iplist.append(alog[8])
                if page_dict.has_key(alog[4]):
                    page_dict[alog[4]] += 1
                else:
                    page_dict[alog[4]] = 1
                l = Logdata(date=alog[0], time=alog[1], s_ip=alog[2], cs_method=alog[3], cs_uri_stem=alog[4], cs_uri_query=alog[5], s_port=alog[6], cs_username=alog[7], c_ip=alog[8], cs_user_agent=alog[9],sc_status=alog[10], sc_substatus=alog[11], sc_win32_status=alog[12], time_taken=alog[13], ip_region='unknown', ip_city='unknown')
                querylist.append(l)
                if len(querylist) >= PRODUCENUM:
                   threading.Thread(target=(Query_Queue_Func(produce,(QUERY_QUEUE,querylist)))).start()
                   del querylist[:]
        logger.info('end handle line %s' %ctime())
        thread_check_id = threading.Thread(target=quick_check_id, args=(iplist,))
        thread_check_id.start()
        thread_region_count = threading.Thread(target=region_count, args=(thread_check_id,))
        thread_region_count.start()
        check_thread.append(thread_region_count)
        return HttpResponse('OK')

def get_quick_check_id(request):
    return HttpResponse(str(iddict_quick))

def get_region_count(request):
    return HttpResponse('%s\n\n%s'%(str(countdict), str(page_dict)))


def region_count(thread,quick=True):
    if quick==True:
        usedict=iddict_quick
    else:
        usedict=iddict
    thread.join()
    logger.info('start region count...')

    for k,v in usedict.items():
        if countdict.has_key(v[0]):
            countdict[v[0]][1] = countdict[v[0]][1]+v[1]
            countdict[v[0]][0].append({k:v[1]})
        else:
            countdict[v[0]] = [[{k:v[1]}], v[1]]
    logger.info('end region count.')



def quick_check_id(iplist):
    num = len(iplist)
    logger.info('logdata num:%s' % num)
    iddict_quick.clear()
    g = (x * 10 for x in range(num // 10))
    ip_num=0
    for i in g:
        logger.info('logdata %s' % i)
        c_ip = iplist[i]
        if iddict_quick.has_key(c_ip):
            iddict_quick[c_ip][1] = iddict_quick[c_ip][1] + 1
        else:
            sleep(0.12)
            iddict_quick[c_ip] = [get_ip(c_ip)['data']['region'], 1]
            ip_num=ip_num+1
    save_ip()
    logger.info('%s,ipnum:%s' % (str(iddict_quick), ip_num))



def get_check_id(request):
    check_id()
    return HttpResponse(str(iddict))

def check_id():
    iddict.clear()
    logdata = Logdata.objects.exclude(c_ip=LIP)
    num = len(logdata)
    logger.info('logdata num:%s'%num)

    g = (x * 10 + 1 for x in range(num//10))
    for i in g:

        c_ip = logdata[i].c_ip
        if iddict.has_key(c_ip):
            sleep(0.12)
            iddict[c_ip][1] = iddict[c_ip][1]+1
        else:
            logger.info('check logdata %s' % i)
            iddict[c_ip] = [get_ip(c_ip)['data']['region'], 1]

    logger.info('%s'%(str(iddict)))

def get_ip(ip):
    qurey = 'ip=%s' % ip
    tp = (SCHEME, NETLOCT, PATH, PARAMS, qurey, FRAGMENT)
    url = urlparse.urlunparse(tp)
    response = urllib.urlopen(url)
    info = json.load(response)
    logger.info('GET: id:%s,region:%s'%(ip, info['data']['region']))
    return info

def save_ip():
    #ipsavelist=[]
    #for k,v in iddict_quick.items():
     #   i=Clientip(ip=k, region=v[0], accesstimes=v[1] )
     #   ipsavelist.append(i)
    #update_ip()
    #Clientip.objects.bulk_create(ipsavelist)
    pass

def update_ip():
    #ip_region.clear()
    #lst=Clientip.objects.all()
    #for i in lst:
     #   ip_region[i[0]]=i[1]
    #logger.info('update ip-region list')
    pass

def save_analyze_message():
    pass

def save():
    pass











