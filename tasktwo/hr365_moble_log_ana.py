#coding=utf-8
import os
import sys
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tasktwo.settings")
django.setup()

import json
from logana.testip import get_ip,get_city,get_region
from logana.models import Clientip
from time import sleep
from Queue import Queue
import threading
import logging
from exceptions import KeyError



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
IPLIST=[]
IPREGIONQUEUE=Queue(100000)
IPDICT={}
threadmain=Queue(2)
threadsearch=[]
dict3={}
searchnum={}

filelist=['/home/jsw/DianMi.HR365-API-2015-07-20.log']
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
                try:
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
                    valueerrornum +=1
        t = threading.Thread(target=check_ipdict)
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
        with open('/home/jsw/dict3.json', 'r') as dict3_js:
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
            json.dump(dict3, dict3_js)

    return dict1

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


def check_ip(ip, num):
    try:

        lst = Clientip.objects.filter(ip=str(ip))
        if dict3.has_key(lst[0].region):
            dict3[lst[0].region] = dict3[lst[0].region] + num
        else:
            dict3[lst[0].region] = num
        logger.info('check in sql')
        searchnum['searchnum'] += 1
    except :
        try:
           ts=threading.Thread(target=search_ip,args=(ip,num))
           threadsearch.append(ts)
        except:
           logger.info('cannot create ts')

def start_search():
    for t in threadsearch:
        sleep(0.12)
        t.start()

def search_ip(ip,num):
    try:
       lst = get_region(ip)
       l = Clientip(ip=lst[0], region=lst[1])
       IPREGIONQUEUE.put(l)
       if IPREGIONQUEUE.qsize() >= 10:
           lst=[]
           for i in range(10):
               lst.append(IPREGIONQUEUE.get())
           Clientip.objects.bulk_create(lst)
       if dict3.has_key(lst[1]):
           dict3[lst[1]] += num
       else:
           dict3[lst[1]] = num
       logger.info('search done')
       searchnum['searchnum'] += 1
    except:
       logger.info('failed')



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




