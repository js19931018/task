from qiniustorage import *
class EmployeeAttachmentSimpleSlim(object):
    def __init__(self, attachment_id, key):
        self.attachment_id=attachment_id
        self.key=key
        self.q=QiniuStorage()
        self.q.get_key(key)
    def start_slim(self):
        r=self.q.persistent_with_pfop('','imageslim')
        return r

class EmploymentAttachmentSlim(object):
    def __init__(self,attachment_id,key,typeid, newupdate=False,thumbnaillargename=None, thumbnailsmallname=None, ):
        self.attachment_id = attachment_id
        self.key = key
        self.q = QiniuStorage()
        self.q.get_key(key)
        self.newupdate = newupdate
        self.thumbnaillargename = thumbnaillargename
        self.thumbnailsmallname = thumbnailsmallname
        self.type = typeid
        if self.type=='1':
            self.slim=EmployeePortraitSlim(self.attachment_id,self.key,self.newupdate,self.thumbnaillargename,self.thumbnailsmallname)
        elif self.type=='2':
            self.slim=EmployeeIdentificationPictureSlim(self.attachment_id,self.key,self.newupdate,self.thumbnaillargename,self.thumbnailsmallname)
        elif self.type=='3':
            self.slim=EmployeeCertificationSlim(self.attachment_id,self.key,self.newupdate,self.thumbnailsmallname)
        elif self.type=='4':
            self.slim=EmployeeCertificateSlim(self.attachment_id,self.key,self.newupdate,self.thumbnailsmallname)
        else :
            self.slim=EmployeeIdentificationSlim(self.attachment_id,self.key,self.newupdate,self.thumbnailsmallname)

    def start_slim(self):
        self.slim.start_slim()




class EmployeePortraitSlim(object):
    def __init__(self,attachment_id,key,newupdate=False,thumbnaillargename=None,thumbnailsmallname=None):
        self.attachment_id = attachment_id
        self.key = key
        self.q = QiniuStorage()
        self.q.get_key(key)
        self.newupdate = newupdate
        self.thumbnaillargename = thumbnaillargename if not thumbnaillargename == None else 'large'
        self.thumbnailsmallname = thumbnailsmallname if not thumbnailsmallname == None else 'small'
    def start_slim(self):

        if self.newupdate:
            r = self.start_slim_get_thumbnail()
        else:
            r = self.q.persistent_with_pfop('', 'imageMogr2/thumbnail/600x600>/size-limit/100k!')
        return r

    def start_slim_get_thumbnail(self):

        fops=['imageMogr2/thumbnail/600x600>/size-limit/100k!',
              'imageView2/2/w/300/h/300/format/jpg/interlace/1',
              'imageView2/2/w/50/h/50/format/jpg/interlace/1']

        perstr = ['', self.thumbnaillargename, self.thumbnailsmallname]
        r = self.q.persistent_with_pfop_nfop(perstr,fops)
        return r

class EmployeeIdentificationPictureSlim(object):
    def __init__(self,attachment_id,key,newupdate=False,thumbnaillargename=None,thumbnailsmallname=None):
        self.attachment_id = attachment_id
        self.key = key
        self.q = QiniuStorage()
        self.q.get_key(key)
        self.newupdate = newupdate
        self.thumbnaillargename = thumbnaillargename if not thumbnaillargename == None else 'large'
        self.thumbnailsmallname = thumbnailsmallname if not thumbnailsmallname == None else 'small'
    def start_slim(self):

        if self.newupdate:
            r = self.start_slim_get_thumbnail()
        else:
            r = self.q.persistent_with_pfop('', 'imageMogr2/thumbnail/1300x900>/size-limit/300k!')
        return r

    def start_slim_get_thumbnail(self):

        fops=['imageMogr2/thumbnail/1300x900>/size-limit/300k!',
              'imageView2/2/w/300/h/300/format/jpg/interlace/1',
              'imageView2/2/w/50/h/50/format/jpg/interlace/1']

        perstr=['', self.thumbnaillargename, self.thumbnailsmallname]
        r = self.q.persistent_with_pfop_nfop(perstr,fops)
        return r

class EmployeeCertificationSlim(object):
    def __init__(self,attachment_id,key,newupdate=False,thumbnailsmallname=None):
        self.attachment_id = attachment_id
        self.key = key
        self.q = QiniuStorage()
        self.q.get_key(key)
        self.newupdate=newupdate
        self.thumbnailsmallname=thumbnailsmallname
    def start_slim(self):
        if self.newupdate:
            r = self.start_slim_get_thumbnail()
        else:
            r = self.q.persistent_with_pfop('', 'imageMogr2/thumbnail/1800x1800>/size-limit/300k!')
        return r

    def start_slim_get_thumbnail(self):

        fops=['imageMogr2/thumbnail/1800x1800>/size-limit/300k!',
              'imageView2/2/w/600/h/600/format/jpg/interlace/1']

        perstr=['',  self.thumbnailsmallname]
        r = self.q.persistent_with_pfop_nfop(perstr,fops)
        return r


class EmployeeCertificateSlim(object):
    def __init__(self, attachment_id, key,newupdate=False, thumbnailsmallname=None):
        self.attachment_id = attachment_id
        self.key = key
        self.q = QiniuStorage()
        self.q.get_key(key)
        self.newupdate = newupdate
        self.thumbnailsmallname = thumbnailsmallname


    def start_slim(self):
        if self.newupdate:
            r = self.start_slim_get_thumbnail()
        else:
            r = self.q.persistent_with_pfop('', 'imageMogr2/thumbnail/1800x1800>/size-limit/700k!')
        return r

    def start_slim_get_thumbnail(self):

        fops = ['imageMogr2/thumbnail/1800x1800>/size-limit/700k!',
                'imageView2/2/w/600/h/600/format/jpg/interlace/1']

        perstr = ['', self.thumbnailsmallname]
        r = self.q.persistent_with_pfop_nfop(perstr, fops)
        return r

class EmployeeIdentificationSlim(object):
    def __init__(self, attachment_id, key,newupdate=False, thumbnailsmallname=None):
        self.attachment_id = attachment_id
        self.key = key
        self.q = QiniuStorage()
        self.q.get_key(key)
        self.newupdate = newupdate
        self.thumbnailsmallname = thumbnailsmallname


    def start_slim(self):
        if self.newupdate:
            r = self.start_slim_get_thumbnail()
        else:
            r = self.q.persistent_with_pfop('', 'imageMogr2/thumbnail/1000x1000>/size-limit/300k!')
        return r

    def start_slim_get_thumbnail(self):

        fops = ['imageMogr2/thumbnail/1800x1800>/size-limit/300k!',
                'imageView2/2/w/300/h/300/format/jpg/interlace/1']

        perstr = ['', self.thumbnailsmallname]
        r = self.q.persistent_with_pfop_nfop(perstr, fops)
        return r








if __name__ == '__main__':
    es=EmployeePortraitSlim('', 'ie_7032c54815e14f9aa8ff3dcc2dcac54c',newupdate=True)
    es.start_slim()




