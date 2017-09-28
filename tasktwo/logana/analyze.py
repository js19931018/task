import json
import re
import logging
from django.http import HttpResponse
from logana.models import Logdata
from exceptions import KeyError

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
loglist=[]
def save_to_sql(alog):
    try:
        if len(alog) == 14:
            l = Logdata(date=alog[0], time=alog[1], s_ip=alog[2], cs_method=alog[3], cs_uri_stem=alog[4], cs_uri_query=alog[5], s_port=alog[6], cs_username=alog[7], c_ip=alog[8], cs_user_agent=alog[9], sc_status=alog[10], sc_substatus=alog[11], sc_win32_status=alog[12], time_taken=alog[13])
            l.save()
            return None
        else:
            logger.debug('not len equal,return to response: %s'%len(alog))
            return alog

    except:
        logger.debug('other problem alog:%s'%alog)





def logrequest(request):
    if request.method == "POST":
        del loglist[:]
        file_l = request.body
        lst = file_l.split('\n')
        logger.debug('nums of log:%s'%len(lst))
        for item in lst:
            alog = item.split()
            r = save_to_sql(alog)
            if r:
                loglist.append(r)
        if loglist == []:
            return HttpResponse('OK')
        else:
            return HttpResponse(loglist)








        return HttpResponse('Get log successful %s \n%s'%(type(file),lst))
    else:
        pass

def save():
    pass











