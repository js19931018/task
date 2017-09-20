import db

class Field(object):
    def __init__(self, name,default,column_type,primary_key,upable):
        self.name = name
        self.column_type = column_type
        self.default=default
        self.primary_key=primary_key
        self.upable=upable
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name,default='',primary_key=False,upable=True):
        super(StringField, self).__init__(name, default,'varchar(100)',primary_key,upable)


class IntegerField(Field):
    def __init__(self, name,default='',primary_key=False,upable=True):
        super(IntegerField, self).__init__(name, default,'bigint',primary_key,upable)

class BooleanField(Field):
    def __init__(self, name,default=0,primary_key=False,upable=True):
        super(BooleanField, self).__init__(name, default,'tinyint',primary_key,upable)

class FloatField(Field):
    def __init__(self,name,default=0,primary_key=False,upable=True):
        super(FloatField, self).__init__(name, default,'float',primary_key,upable)

class TextField(Field):
    def __init__(self,name,default='',primary_key=False,upable=True):
        super(TextField, self).__init__(name, default, 'text',primary_key,upable)


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.iteritems():  #k represents attributes name,v represents attributes value of THE CLASS
            if isinstance(v, Field):#add some attributes of subclass of Model to dict mapping
                print('Found mapping: %s==>%s' % (k, v))#name of attributes of subclass of Model->instance of Field
                mappings[k] = v
        for k in mappings.iterkeys(): #use key to get a value in dict
            attrs.pop(k)         #pop(key) to delete
        attrs['__table__'] = name #subclass of Model's name
        attrs['__mappings__'] = mappings
        return type.__new__(cls, name, bases, attrs)

class Model(dict):
    __metaclass__ = ModelMetaclass  #why use metaclass: we use attribute __table__ __mapping__ we dont know its value ,it depends on Model subclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def create_table(self):
        field_c=[]
        for k,v in self.__mappings__.iteritems():
            print v
            if v.primary_key==True:
                str_pri='primary key'
            else:
                str_pri=''
            str_c='%s %s %s %s' %(v.name,v.column_type,'not null',str_pri)
            field_c.append(str_c)
        sql='create table %s (%s)' %(self.__table__,','.join(field_c))
        db.update(sql)
        print('SQL: %s' % sql)




    def insert_one(self):
        fields = []
        params = []
        args = []
        args_str=[]
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            if getattr(self, k, None) == None:
                args.append(v.default)#instance attributes in args,not class attributes
            else:
                args.append(getattr(self, k, None))
        for l in args:
            args_str.append("'"+str(l)+"'")

        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(args_str))
        print('SQL: %s' % sql)
        db.insert(sql)   #Attribute __table__ is from Modelmetaclass
        print('ARGS: %s' % str(args))

    def select_one(self,kid,key):

        sql = "select * from %s where %s='%s'" % (self.__table__,kid,key)
        s=db.select(sql)
        print 'selelct sql: %s' % sql # Attribute __table__ is from Modelmetaclass
        print 'select result: %s'%str(s)
        if s:                #s is a list containing only one return from db.select
            return s[0]
        else:
            return s

    def select_some(self,kid,key):
        sql = "select * from %s where %s='%s'" % (self.__table__, kid, key)
        s = db.select(sql)
        print 'selelct sql: %s' %sql  # Attribute __table__ is from Modelmetaclass
        print 'select result: %s' %str(s)
        return s



    def update_one(self,kid,key,cid,change):
        for k, v in self.__mappings__.iteritems():
            if cid==v.name:
                if v.upable==False:
                    print ('cannot update this')
                else:
                    sql= "update %s set %s='%s' where %s='%s'"% (self.__table__,cid,change,kid,key)
                    db.update(sql)
                    print('SQL: %s' % sql)

    def delete_one(self,kid,key):
        sql="delete from %s where %s='%s'" %(self.__table__,kid,key)
        print('SQL: %s' % sql)

    def select(self):

        sql = "select * from %s " % (self.__table__)
        s=db.select(sql)
        print('SQL: %s' % sql)  # Attribute __table__ is from Modelmetaclass
                        #s is a list containing only one return from db.select
        return s      # a list containing nums of dicts

    def select_by(self,order_id,str):

        sql = "select * from %s order by %s %s" % (self.__table__,order_id,str)
        print('SQL: %s' % sql)
        s = db.select(sql)
          # Attribute __table__ is from Modelmetaclass
        # s is a list containing only one return from db.select
        return s  # a list containing nums of dicts

    def count(self):
        sql = "select count(*) as num from %s" % (self.__table__,)
        s = db.select(sql)
        print('SQL: %s' % sql)  # Attribute __table__ is from Modelmetaclass
        # s is a list containing only one return from db.select

        r=s[0]
        return r['num']

if __name__ == '__main__':
    class User(Model):
        id = IntegerField('id',default=123456,primary_key=True,upable=False) #instance of Field such as id.name,id.default
        name = StringField('username',default='enteryouname',primary_key=False,upable=True)
        email = StringField('email',default=None,primary_key=False,upable=True)
        password = StringField('password',default='123456',primary_key=False,upable=True)


    db.logging.basicConfig(level=db.logging.DEBUG)
    db.create_engine('www-data', 'www-data', 'test')
    u = User(id=12345, email='test@orm.org', password='my-pwd')
    #u.create_table()
    #u.insert_one()
    sel=u.select_one('id','12345')

    u.update_one('id','12345','password','666666')






