#coding=utf-8
import urlparse,urllib,json
from datetime import time
from datetime import date
import requests


scheme = 'http'
netloct = 'eeboframework-v2.eebochina.com:9015'
path = '/locateit/location/ip'
params = ''
fragment = ''
mydict={'1':[1,2,3], '2':[4,5,6]}

def get_ip(ip):
    qurey=''

    tp=(scheme, netloct, path, params, qurey, fragment)
    url=urlparse.urlunparse(tp)
    res=requests.get('http://api.2haohr.com/ipservice/query/',params={'ip':ip})
    r=json.loads(res.text)
    return r
'''
def get_city(ip):
    try:
        res=get_ip(ip)
        return [ip, res['data']['city_id']]
    except:
        pass
'''
def get_region(ip):
    try:
        res = get_ip(ip)
        return [ip, res['data']['province']]
    except:
        pass



def time():
    timestr='08:03:16'

if __name__ == '__main__':
   print get_region('117.136.1.254')
