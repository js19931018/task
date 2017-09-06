import time, uuid
import db
import transwarp_orm

from db import next_id
from transwarp_orm import Model, StringField, BooleanField, FloatField, TextField

class User(Model):
    __table__ = 'User'

    id = StringField('id',default=next_id)
    email = StringField('email',upable=False )
    password = StringField('password')
    admin = BooleanField('admin')
    name = StringField('name')
    image = StringField('image')
    created_at = FloatField('create_at',default=time.time())

class Blog(Model):
    __table__ = 'Blog'

    id = StringField( 'id',primary_key=True, default=next_id)
    user_id = StringField('user_id',upable=False)
    user_name = StringField('use_name')
    user_image = StringField('user_image')
    name = StringField('name')
    summary = StringField('summary')
    content = TextField('content')
    created_at = FloatField('create_at',upable=False, default=time.time())

class Comment(Model):
    __table__ = 'Comment'

    id = StringField( 'id',default=next_id)
    blog_id = StringField('blog_id')
    user_id = StringField('user_id')
    user_name = StringField('username')
    user_image = StringField('user_image')
    content = TextField('content')
    created_at = FloatField('create_at')

if __name__ == '__main__':
    db.logging.basicConfig(level=db.logging.DEBUG)
    db.create_engine('www-data', 'www-data', 'test')

    u = User(id=12345, admin='1',name='jsw',email='1736219667@qq.com', password='my-pwd')
    u.create_table()
    u.insert_one()
    u.select_one('id','12345')
    u.update_one('id','12345','password','666666')

    b=Blog(id=1, user_id='12345',name='first_blog',user_name='jsw')
    b.create_table()

    c=Comment()
    c.create_table()