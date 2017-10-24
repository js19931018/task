#coding=utf-8
import os
import sys
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tasktwo.settings")
django.setup()
from logana.models import *
from hr365_moble_log_ana import *
TESTIPDICT1={'183.38.74.92':10,
             '183.38.75.92':10,
             '119.131.207.188':10}

TESTIPDICT2={'183.38.74.92':10,
             '10.10.251.212':10,
             '110.174.12.219':10

}

#change database to testlogmessage first

class Test_Single_Log(object):
    def __init__(self):
        self.testdict=TESTIPDICT1
    def start_test(self):
        IPDICT.clear()
        dict3.clear()
        dict4.clear()
        filelist.append('Test_Single_Log')
        for k, v in self.testdict.items():
           IPDICT[k] = v
        check_ipnet()
        llp=Ipnet.objects.all()
        llp_d={}
        for i in llp:
            llp_d[i.ip]=[i.net]
        lnr=Netregion.objects.all()
        lnr_d={}
        for i in lnr:
            lnr_d[i.net]=[i.region,i.iptype,i.version]
        lrc=Regioncount.objects.all()
        lrc_d={}
        for i in lrc:
            lrc_d[i.id]=[i.region,i.num,i.logdatename]
        return {'Ipnet':llp_d,'Netregion':lnr_d,'Regioncount':lrc_d}

class Test_New_Log(object):   #test after the first log analyzed and saved,
    def __init__(self):
        self.testdict = TESTIPDICT2

    def start_test(self):
        IPDICT.clear()
        dict3.clear()
        dict4.clear()
        filelist.append('Test_Single_Log')
        for k, v in self.testdict.items():
            IPDICT[k] = v
        check_ipnet()
        llp = Ipnet.objects.all()
        llp_d = {}
        for i in llp:
            llp_d[i.ip] = [i.net]
        lnr = Netregion.objects.all()
        lnr_d = {}
        for i in lnr:
            lnr_d[i.net] = [i.region, i.iptype, i.version]
        lrc = Regioncount.objects.all()
        lrc_d = {}
        for i in lrc:
            lrc_d[i.id] = [i.region, i.num, i.logdatename]
        return {'Ipnet': llp_d, 'Netregion': lnr_d, 'Regioncount': lrc_d}

class Test_With_Same_Ip(object): #save and analyze with same ipdict 10 times
    def __init__(self):
        pass

    def start_test(self):
        for i in range(10):
           t=Test_Single_Log()
           t.start_test()

        check_ipnet()
        llp = Ipnet.objects.all()
        llp_d = {}
        for i in llp:
            llp_d[i.ip] = [i.net]
        lnr = Netregion.objects.all()
        lnr_d = {}
        for i in lnr:
            lnr_d[i.net] = [i.region, i.iptype, i.version]
        lrc = Regioncount.objects.all()
        lrc_d = {}
        for i in lrc:
            lrc_d[i.id] = [i.region, i.num, i.logdatename]
        return {'Ipnet': llp_d, 'Netregion': lnr_d, 'Regioncount': lrc_d}






