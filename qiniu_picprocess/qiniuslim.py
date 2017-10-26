from qiniustorage import *
class EmployeeAttachmentSlim(object):
    def __init__(self,attachment_id,key):
        self.attachment_id=attachment_id
        self.key=key
        self.q=QiniuStorage()
        self.q.get_key(key)
    def start_slim(self):
        r=self.q.persistent_with_pfop('','imageslim')
        return r

class EmployeePortraitSlim(object):
    def __init__(self,attachment_id,key,newupdate=False,thumbnaillargename=None,thumbnailsmallname=None):
        self.attachment_id = attachment_id
        self.key = key
        self.q = QiniuStorage()
        self.q.get_key(key)
        self.newupdate=newupdate
        self.thumbnaillargename=thumbnaillargename if not thumbnaillargename == None else 'large'
        self.thumbnailsmallname=thumbnailsmallname if not thumbnailsmallname == None else 'small'
    def start_slim(self):

        if self.newupdate:
            r = self.start_slim_get_thumbnail()
        else:
            r = self.q.persistent_with_pfop('', 'imageMogr2/thumbnail/600x600>/size-limit/100k!')
        return r

    def start_slim_get_thumbnail(self):

        fops=['imageMogr2/thumbnail/600x600>/size-limit/100k!',
              'imageView2/w/300/h/300',
              'imageView2/w/50/h/50']

        perstr=['', self.thumbnaillargename, self.thumbnailsmallname]
        r = self.q.persistent_with_pfop_nfop(perstr,fops)
        return r




class EmployeeAttachmentUpadateSlim(object):
    pass



if __name__ == '__main__':
    es=EmployeeAttachmentSlim('','ie_ae54459e3968430486f35576a6535921')
    es.start_slim()




