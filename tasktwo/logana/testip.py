#coding=utf-8
import urlparse,urllib,json
from datetime import time
from datetime import date
import requests


scheme = 'http'
netloct = 'ip.taobao.com'
path = '/service/getIpInfo.php'
params = ''
fragment = ''
mydict={'1':[1,2,3], '2':[4,5,6]}

def get_ip(ip):
    qurey='ip=%s'%ip
    tp=(scheme, netloct, path, params, qurey, fragment)
    url=urlparse.urlunparse(tp)
    print url
    response=urllib.urlopen(url)
    info=json.load(response)
    print info
    return info

def time():
    timestr='08:03:16'

if __name__ == '__main__':
    for k,v in mydict.items():
        print k,v