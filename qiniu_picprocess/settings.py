import time


QINIU_ACCESS_KEY='Yim6E1qQZbqjF46RUO4RltWRNriH8rrBIxDoROdD'
QINIU_SECRET_KEY='BAoUH7wZjPDIQLpBpiMqxGgjXCRnof4fvGDLSd2b'
QINIU_PRIVATE_BUCKET_NAME='processimg-slim'
QINIU_PRIVATE_DOMAIN='oy9j1chwz.bkt.clouddn.com'
QINIU_CALLBACK='http://adminapi-dev.2haohr.com/cs/home/callback/'
QINIU_PUT_POLICY={'scope': 'processimg-slim',
                  'deadline': '%s'%(int(time.time()+3600)),
                  'persistentOps': '',
                  'persistentNotifyUrl':  'http://fake.com/qiniu/notify'

}
QINIU_PIPELINE = ''
QINIU_PFOP_NOTIFYURL=''