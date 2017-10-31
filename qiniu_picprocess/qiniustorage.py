# -*- coding: utf-8 -*-
from qiniu import Auth,put_data
from qiniu.utils import urlsafe_base64_encode
from qiniu.services.processing.pfop import PersistentFop
import requests
import urllib
import settings
import uuid
class QiniuStorage(object):



    def __init__(self):  #instanciate a Auth object with AK,SK
        self.q = Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)
        self.bucket = settings.QINIU_PRIVATE_BUCKET_NAME
        self.domain = settings.QINIU_PRIVATE_DOMAIN
        self.key=None
    def upload_token(self, ie=False):     #got a token coding with policy and SK,when updating with policy ,it must get a corresponding token
        key = str(uuid.uuid4()).replace('-', '')
        key = 'ie_' + key if ie else key
        return key, self.q.upload_token(self.bucket, key=key)

    def upload_data(self, data, mime_type='application/octet-stream', ie=True): #using it to upload a data
        key, token = self.upload_token(ie)
        ret, info = put_data(token, key, data, mime_type=mime_type)
        self.key = key
        if ret['key'] != key:          # key is the key of the updated data
            raise Code.file_update_fail
        return key

    def view_url(self, key, style=None):
        if style:
            base_url = '{}{}!{}'.format(self.domain, key, style)
        else:
            base_url = '{}{}'.format(self.domain, key)
        # return self.q.private_download_url(base_url)
        return base_url

    def down_url(self, key, file_name=None):
        file_name = "?attname=" + urllib.quote(file_name.encode(
            'utf8')) if file_name else ''
        url='%s%s'%("?{}".format(key),"?{}".format(file_name)) if file_name else "/{}".format(key)

        base_url = 'http://'+self.domain+url
        return self.q.private_download_url(base_url)

    def download(self, key):
        url = self.down_url(key)
        r = requests.get(url)
        if r.status_code != 200:
            raise Code.file_update_fail
        return r.content

    def verify_callback(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION', None)
        return self.q.verify_callback(auth, settings.QINIU_CALLBACK,
                                      request.body)

    def persistent_with_pfop(self,perstr,fops):#persistenet operations with fop sentence.the result save as 'origin key+perstr'
        auth = self.q
        bucket_name = self.bucket
        saveas_key = self.key + perstr
        entryuri=settings.QINIU_PRIVATE_BUCKET_NAME+':'+saveas_key
        entryuri=urlsafe_base64_encode(entryuri)
        fops = fops + '|saveas/{}'.format(entryuri)

        pfop = PersistentFop(auth,bucket_name,pipeline=settings.QINIU_PIPELINE)
        ret, info=pfop.execute(self.key, [fops], 1)
        return [ret,info]

    def persistent_with_pfop_nfop(self,perstr,fops):#persistent fop operation with nums of fop execute sentence
        auth = self.q
        bucket_name =self.bucket
        foplist=[]
        for i in range(len(fops)):
            saveas_key = self.key + perstr[i]
            entryuri = settings.QINIU_PRIVATE_BUCKET_NAME + ':' + saveas_key
            entryuri = urlsafe_base64_encode(entryuri)
            fop = fops[i] + '|saveas/{}'.format(entryuri)
            foplist.append(fop)
        pfop = PersistentFop(auth, bucket_name, pipeline=settings.QINIU_PIPELINE)
        ret, info = pfop.execute(self.key, foplist, 1)
        return [ret, info]


    def get_key(self,key):
        self.key=key

class Code(object):

    file_update_fail = ''
