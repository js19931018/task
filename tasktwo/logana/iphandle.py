from IPy import *
from logana.testip import get_region
def handleip(ipdict):
    netdict={}
    ipnetdict={}
    for ip,num in ipdict.items():
       ip_net =str(ip.split('.')[0]+'.'+ip.split('.')[1]+'.'+'0'+'.'+'0')
       ipnetdict[ip] = ip_net
       if netdict.has_key(ip_net):
           netdict[ip_net]['num'] += num
       else:
           netdict[ip_net] = {'num':num,'iptype': IP(ip).iptype(), 'version':IP(ip).version()}
    print netdict
    return [ipnetdict, netdict]

def singleip(ip,num):
    ip_net = str(ip.split('.')[0] + '.' + ip.split('.')[1] + '.' + '0' + '.' + '0')
    return {ip_net:{'num':num, 'iptype': IP(ip).iptype(), 'version':IP(ip).version()}}

if __name__ == '__main__':
    handleip({'220.122.122.19':3})

