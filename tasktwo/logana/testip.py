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
    response=requests.get(url, timeout=15)
    info=json.loads(response.text)
    print info
    return info

def get_city(ip):
    try:
        res=get_ip(ip)
        return [ip, res['data']['city_id']]
    except:
        pass

def get_region(ip):
    try:
        res = get_ip(ip)
        return [ip, res['data']['region_id']]
    except:
        pass



def time():
    timestr='08:03:16'

if __name__ == '__main__':
   print get_city('117.136.1.254')
