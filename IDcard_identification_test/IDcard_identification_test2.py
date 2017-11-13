#  -*- coding: utf-8 -*-


from shenfenzheng5 import *
import pickle
import time
from exceptions import AssertionError
errmessage={'checkdate': '身份证日期检测错误',
            'checklen':'长度检测错误',
            'checkcity':'所在地区检测错误',
            'checkbyte':'校验位检测错误',
            'checksex':'性别检测错误'

        }

TestfuncReturn={'checkdate': ['date incorrect', '出生日期%s年%s月%s日'],
                'checklen': ['long incorrect', 'long correct'],
                'checkcity':['region incorrect', '发证地区：%s%s%s'],
                'checkbyte':['verify incorrect', 'verify correct'],
                'checksex':['male','female', 'sexerr']


}

ctime=time.strftime('%Y%m%d', time.localtime(time.time()))
tstdictcheckdate={}
tstdictcheckLen={}
tstdictcheckCity={}
tstdictcheckByte={}
tstdictchecksex={}

class IdentifyError(Exception):
    def __init__(self,errtype,id,res,asrt_res):
        self.message='%s,测试身份证号:%s\n测试应该的结果：%s\n测试结果:%s\n'%(errmessage[errtype],id,res,asrt_res)
        print self.message

class TestId(object):
    def __init__(self,method,tstdict):
        self.method=method
        self.tstdict=tstdict
        self._start_test()

    def _start_test(self):
        for k,v in self.tstdict.items():
            try:
                assert v==self.method(k)
            except AssertionError,e:
                raise IdentifyError(self.method.__name__, k, v, self.method(k))

def get_ctime():
    return time.strftime('%Y%m%d', time.localtime(time.time()))

def checkdate_sample():
    ctime = int(get_ctime())
    trueid ='320102199310182019'
    err1=['320102%s2019'%str(ctime+i*10000) for i in range(5)]  #当前日期的未来时间检测
    err2=['320102%s2019'%str(ctime-i*10000) for i in range(5)]  #当前日期的最近五年检测
    err1_month_id='320102199316182019'                        #错误的月
    err1_year_id='320102299316182019'                         #错误的年份
    err1_day_id='320102199310382019'                          #错误的日
    corr1=['320102%s2019'%str(ctime-i*10000) for i in range(16, 21)]   #正确并可能的18位身份证日期

    corr_15_id='320102931018201'                                       #正确并可能的18位身份证日期
    err1_15_month_id='320102934018201'                                 #错误的月
    err1_15_day_id='320102931048201'                                   #错误的日
    tstdictcheckdate[trueid]=TestfuncReturn['checkdate'][1]%('1993','10','18') #整理并测试
    for i in err1:
        tstdictcheckdate[i] = TestfuncReturn['checkdate'][0]
    for i in err2:
        tstdictcheckdate[i] = TestfuncReturn['checkdate'][0]
    for i in corr1:
        tstdictcheckdate[i] = TestfuncReturn['checkdate'][1] % (i[6]+i[7]+i[8]+i[9], i[10]+i[11], i[12]+i[13])
    tstdictcheckdate[corr_15_id] = TestfuncReturn['checkdate'][1] % ('1993', '10', '18')
    tstdictcheckdate[err1_day_id] =TestfuncReturn['checkdate'][0]
    tstdictcheckdate[err1_year_id] = TestfuncReturn['checkdate'][0]
    tstdictcheckdate[err1_month_id] = TestfuncReturn['checkdate'][0]
    tstdictcheckdate[err1_15_day_id] = TestfuncReturn['checkdate'][0]
    tstdictcheckdate[err1_15_month_id] = TestfuncReturn['checkdate'][0]

def checklen_sample():
    trueid='320102199310182019'
    for i in range(14):
        tstdictcheckLen[trueid[0:i]]=TestfuncReturn['checklen'][0]
    for i in range(15,17):
        tstdictcheckLen[trueid[0:i]] = TestfuncReturn['checklen'][0] #非正常的长度校验
    tstdictcheckLen[trueid] = TestfuncReturn['checklen'][1]          #18位
    tstdictcheckLen[trueid[0:14]]=TestfuncReturn['checklen'][1]      #15位
    tstdictcheckLen['']=TestfuncReturn['checklen'][0]                #空字符
    tstdictcheckLen['3201021993101820191'] = TestfuncReturn['checklen'][0]   #过长

def checkCity_sample():
    trueid='320102199310182019'
    tstdictcheckLen[trueid] = TestfuncReturn['checkcity'][1]%('江苏省','南京市','玄武区') #正确
    tstdictcheckLen['50'+trueid[2:17]] = TestfuncReturn['checkcity'][0]      #三级行政编码均不正确
    tstdictcheckLen[trueid[0:1] + '40' + trueid[4:17]] = TestfuncReturn['checkcity'][0]
    tstdictcheckLen[trueid[0:3] + '99' + trueid[6:17]] = TestfuncReturn['checkcity'][0]

def checkByte_sample():
    verifycode=['1','2','3','4','5','6','7','8','9','X']
    trueid = '320102199310182019'
    verifycode.remove(trueid[17])
    tstdictcheckLen[trueid] = TestfuncReturn['checkcity'][1]
    for i in verifycode:
        tstdictcheckLen[trueid[0:16]+str(i)] = TestfuncReturn['checkcity'][0]


def checksex():
    trueid = '320102199310182019'
    male=['1','3','5','7','9']
    female=['0','2','4','6','8']
    for i in female:
        tstdictcheckLen[trueid[0:15]+i+trueid[17]] = TestfuncReturn['checksex'][1]
    for i in male:
        tstdictcheckLen[trueid[0:15]+i+trueid[17]] = TestfuncReturn['checksex'][0] #十八位身份证性别校验
    for i in female:
        tstdictcheckLen[trueid[0:5]+trueid[7:13]+i] = TestfuncReturn['checksex'][1]
    for i in male:
        tstdictcheckLen[trueid[0:5] + trueid[7:13] + i] = TestfuncReturn['checksex'][0]#十五位身份证性别校验






def testall():
   # checkdate_sample()
   # t=TestId(checkdate, tstdictcheckdate)
    checklen_sample()
    t = TestId(checklen, tstdictcheckLen)
    checkdate_sample()
    t = TestId(checkcity, tstdictcheckCity)
    checkdate_sample()
    t = TestId(checkbyte, tstdictcheckByte)
    checkdate_sample()
    t = TestId(checksex, tstdictchecksex)
    










if __name__ == '__main__':
   testall()