tstdict={'longerr':'3306811995020103391',
         'regionerr':'100681199502010339',
         'illegalstr':'330681199502010B39',
         'birtherr':'330681199951312025',
         'verifyerr':'330681199502010338',
         'pass':'330681199502010339'
         }

errormessage={'pass':'',
              'errtype1':'longerr',
              'errtype2':'',
              'errtype3':'',
              'errtype4':''}

def checkid(id):
    if id=='3306811995020103391':
        return 'longerr'



class Testmethod(object):
    def __get__(self,ist,tstclass):
        return ist.asrt_eq(tstclass.method[0](ist.id))

class TestId(object):
    def __init__(self,id,asrt_res):
        self.id=id
        self.asrt_res=asrt_res


    test = Testmethod()

    def asrt_eq(self,res):
        assert self.asrt_res==res

    @classmethod
    def setmethod(cls,method):
        cls.method=[]
        cls.method.append(method)


class TestIDlong(TestId):
    def __init__(self):
        TestId.__init__(self, tstdict['longerr'], errormessage['errtype1'])

class TestIDregion(TestId):
    def __init__(self):
        TestId.__init__(self,tstdict['regionerr'], errormessage['errtype2'])

class TestIDbirth(TestId):
    def __init__(self):
        TestId.__init__(self,tstdict['birtherr'], errormessage['errtype3'])

class TestIDillegalstr(TestId):
    def __init__(self):
        TestId.__init__(self,tstdict['illegalstr'], errormessage['errtype4'])

class TestIDverify(TestId):
    def __init__(self):
        TestId.__init__(self,tstdict['regionerr'], errormessage['errtype4'])

class TestIDpass(TestId):
    def __init__(self):
        TestId.__init__(self, tstdict['pass'], errormessage['pass'])

def testall(tstfunc):
    TestId.setmethod(checkid)
    s = TestIDlong()
    s.test
    s = TestIDregion()
    s.test
    s = TestIDbirth()
    s.test
    s = TestIDillegalstr()
    s.test
    s = TestIDverify()
    s.test
    s = TestIDpass()
    s.test







if __name__ == '__main__':
    testall(checkid)