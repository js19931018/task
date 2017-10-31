# -*- coding: utf-8 -*-
from qiniustorage import *
from io import StringIO,BytesIO
import requests
class Qiniuupdate(object):
    def __init__(self,filepath):
        self.filepath=filepath
        with open(self.filepath) as file:
            self.file=file
            self.output=BytesIO(self.file.read())
        self.q = QiniuStorage()
        self.key =None
      # self.output.write(self.file)
    def get_url(self,filename):
        self.q = QiniuStorage()
        self.key=self.q.upload_data(self.output.getvalue())
        down_url = self.q.down_url(self.key,file_name=None)
        return down_url
    def imgview(self, mode, w, h):
        fops = 'imageView2/%s/w/%s/h/%s'%(mode, w, h)
        r=self.q.persistent_with_pfop('imgview2mode%sw%sh%s'%(mode, w, h),fops)
        return r

def get_a_down_url():
    q=QiniuStorage()
    r=q.down_url('ie_0ea63c5d287840b2a9600701d8306f3e?imageInfo')
    re=requests.get(r)
    return re
if __name__ == '__main__':
  r=get_a_down_url()
#q=Qiniuupdate('/home/jsw/bigimg1.jpeg')
#t=q.get_url('bigimg1')
#print t
#h=q.imgview(0,64,48)