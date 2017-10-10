#coding=utf-8
import urlparse,urllib,json




scheme = 'http'
netloct = 'ip.taobao.com'
path = '/service/getIpInfo.php'
params = ''
fragment = ''


def get_ip(ip):
    qurey='ip=%s'%ip
    tp=(scheme, netloct, path, params, qurey, fragment)
    url=urlparse.urlunparse(tp)
    print url
    response=urllib.urlopen(url)
    info=json.load(response)
    print info
    return info


if __name__ == '__main__':
    get_ip('113.91.87.185')
    print u'\u5e7f\u4e1c\u7701'.encode('utf-8')
    print '亚马逊'

