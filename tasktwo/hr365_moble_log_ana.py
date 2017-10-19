#coding=utf-8
import os
import sys
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tasktwo.settings")
django.setup()

import json
from logana.testip import get_ip, get_region
from logana.models import Netregion,Ipnet,Regioncount
from time import sleep
from Queue import Queue
import threading
import logging
from exceptions import KeyError
from IPy import *
from logana.iphandle import handleip,singleip



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
IPLIST=[]
IPREGIONQUEUE=Queue(100000)
IPDICT={}
threadmain=Queue(2)
threadsearch=[]
dict3={}   #netregion-dict {ipnet1:{ version:xxx ,region:xxx, iptype:xxx}...}
dict4={}   #region-dict {region1:num...}
searchnum={}

filelist=['/home/jsw/DianMi.HR365-API-2015-07-31.log']


def openfile(list):
    with open('/home/jsw/dict1.json','r') as dict1_js:
       try:
            dict1=json.load(dict1_js)
            logger.info('dict1 %s'%dict1)
       except:
            dict1={}


    totalnum=0
    handlenum=0
    keyerrornum=0
    valueerrornum=0
    dict3.clear()
    for i in list:
        file=open(i)
        f=file.read()
        lst=f.split()
        for items in lst:
            if items[0]=='{':
                '''try:
                    totalnum +=1
                    js = json.loads(items)
                    if dict1.has_key(str(js['actionlog_item']['action_params']['city_id'])) :
                        if dict1[str(js['actionlog_item']['action_params']['city_id'])].has_key(str((js['user_id']))):
                            dict1[str(js['actionlog_item']['action_params']['city_id'])][str(js['user_id'])]+=1
                        else:
                            dict1[str(js['actionlog_item']['action_params']['city_id'])][str(js['user_id'])]=1
                    else:
                        dict1[str(js['actionlog_item']['action_params']['city_id'])]={str(js['user_id']):1}
                    handlenum +=1
                except KeyError:
                    keyerrornum +=1
                    try:
                        if IPDICT.has_key(js['actionlog_item']['ip']):
                            IPDICT[js['actionlog_item']['ip']]+=1
                        else:
                            IPDICT[js['actionlog_item']['ip']] = 1
                    except:
                        pass
                except ValueError:
                    valueerrornum +=1'''
                try:
                    totalnum += 1
                    js = json.loads(items)
                    if IPDICT.has_key(js['actionlog_item']['ip']):
                        IPDICT[js['actionlog_item']['ip']] += 1
                    else:
                        IPDICT[js['actionlog_item']['ip']] = 1
                except KeyError:
                    keyerrornum += 1
                except ValueError:
                    valueerrornum += 1
        t = threading.Thread(target=check_ipnet)
        threadmain.put(t)
        t.start()
        with open('/home/jsw/dict1.json', 'w') as dict1_js:
            json.dump(dict1, dict1_js)
        with open('/home/jsw/dict2.json', 'r') as dict2_js:
            dict2 = json.load(dict2_js)
            dict2['totalnum']=dict2['totalnum']+totalnum
            dict2['handlenum']=dict2['handlenum']+handlenum
            dict2['errornum']['keyerrornum']+=keyerrornum
            dict2['errornum']['valueerrornum']+=valueerrornum
        with open('/home/jsw/dict2.json', 'w') as dict2_js:
            json.dump(dict2, dict2_js)
        t.join()
        with open('/home/jsw/dict2.json', 'r') as dict2_js:
            dict2 = json.load(dict2_js)
            dict2['searchnum']=dict2['searchnum']+searchnum['searchnum']
        with open('/home/jsw/dict2.json', 'w') as dict2_js:
            json.dump(dict2, dict2_js)
        '''with open('/home/jsw/dict3.json', 'r') as dict3_js:
            try:
                dict3_ori = json.load(dict3_js)
            except:
                dict3_ori={}
        with open('/home/jsw/dict3.json', 'w') as dict3_js:
            for k,v in dict3_ori.items():
                if dict3.has_key(k):
                    dict3[k]=dict3_ori[k]+dict3[k]
                else:
                    dict3[k]=dict3_ori[k]
            json.dump(dict3, dict3_js)'''

    #return dict1

def check_ipdict():
    searchnum['searchnum']=0
    logger.info('start check ipdict')
    logger.info('%s'%IPDICT)
    for ip, num in IPDICT.items():
        check_ip(ip, num)
    logger.info('check_ip finished')
    logger.info('%s'%len(threadsearch))
    start_search()
    for t in threadsearch:
        t.join()

def check_ipnet():
    searchnum['searchnum'] = 0
    ipdict_not_in_sql={}
    lst_ipnet=[]   #Ip-net to save in sql
    lst_netregion=[] #net-region etc to save in sql
    lst_regioncount=[] #regioncount  to save in sql
    for ip, num in IPDICT.items():
       try:
            ipnet=Ipnet.objects.get(ip=ip)
            netregion = Netregion.objects.get(net=ipnet.net)
            if dict4.has_key(netregion.region):
                dict4[netregion.region] = dict4[netregion.region] + num
            else:
                dict4[netregion.region] = num
            logger.info('find ipnet in sql')
       except:

            ipdict_not_in_sql[ip] = num    #ipdict  {ip1:num...}


    iphandle=handleip(ipdict_not_in_sql)
    for ip, net in iphandle[0].items():
        lst_ipnet.append(Ipnet(ip=ip, net=net))
    Ipnet.objects.bulk_create(lst_ipnet)

    for ip_net, v in iphandle[1].items():#start to use check_ip(net-region) in sql or internet
        check_ip(ip_net, v['num'], v['iptype'], v['version'])
    start_search()
    for t in threadsearch:
        t.join()

    for k, v in dict3.items():
        lst_netregion.append(Netregion(net=k, version=v['version'], region=v['region'], iptype=v['iptype']))
    Netregion.objects.bulk_create(lst_netregion)

    for k, v in dict4.items():
        lst_regioncount.append(Regioncount(region=k,num=v,logdatename=filelist[0]))
    Regioncount.objects.bulk_create(lst_regioncount)



def check_ip(ip, num, iptype, version): #try count netregion in sql,write in dict4
    try:
        netregion = Netregion.objects.get(net=str(ip))   #search netregion in sql,only update regioncount dict
        '''if dict3.has_key(lst[0].region):
            dict3[lst[0].region] = dict3[lst[0].region] + num
        else:
            dict3[lst[0].region] = num'''
        if dict4.has_key(netregion.region):
            dict4[netregion.region] = dict4[netregion.region] + num
        else:
            dict4[netregion.region] = num
        logger.info('check in sql Netregion')
        searchnum['searchnum'] += 1
    except:
        try:  #search sql failed ,check this netregion in internet update net-region and region-count
           ts=threading.Thread(target=search_ip, args=(ip, num, version, iptype))
           threadsearch.append(ts)
        except:
           logger.info('cannot create ts')

def start_search():
    for t in threadsearch:
        sleep(0.12)
        t.start()

def search_ip(ip,num,version,iptype):   #ipnet with number update both net-region dict and regioncount dict
    try:    #add a new netregion to dict 3
       if version =='PRIVATE':
          dict3[ip] = {'version': version, 'region': 'private', 'iptype': iptype}
       else:
          lst = get_region(ip)   #search in internet
       dict3[ip]= {'version':version,'region':lst[1],'iptype':iptype}

       '''l = Netregion(net=lst[0], region=lst[1], version=version, iptype=iptype, num=num)
       IPREGIONQUEUE.put(l)
       if IPREGIONQUEUE.qsize() >= 10:
           lst=[]
           for i in range(10):
               lst.append(IPREGIONQUEUE.get())
           Netregion.objects.bulk_create(lst)'''
       if dict4.has_key(lst[1]):         #update region number in dict4
           dict4[lst[1]] += num
       else:
           dict4[lst[1]] = num
       logger.info('search done')
       searchnum['searchnum'] += 1
    except:
       dict3[ip] = {'version': version, 'region': 'unknown', 'iptype': iptype}
       logger.info('failed to search')



def get_result():
    with open('/home/jsw/dict1.json', 'w') as dict1_js:
        dict1=json.load(dict1_js)
    for city, userdict in dict1.items():
        usernum=0
        visitsnum=0
        for k, v in userdict.items():
            usernum += 1
            visitsnum += v
        userdict['usernum']=usernum
        userdict['visitsnum']=visitsnum

    with open('/home/jsw/dict1.json', 'w') as dict1_js:
         json.dump(dict1, dict1_js)

    return dict1


if __name__ == '__main__':
   openfile(filelist)
   #get_result()



