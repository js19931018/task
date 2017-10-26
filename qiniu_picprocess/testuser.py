from qiniustorage import *
from io import StringIO,BytesIO
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



q=Qiniuupdate('/home/jsw/jswimg1.png')
t=q.get_url('jswimg1')
print t
h=q.imgview(0,64,48)