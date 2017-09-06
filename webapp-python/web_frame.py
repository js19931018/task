import time, uuid
import db
import transwarp_orm
import MyModel
import re
import json
import threading
import hashlib
import flask
import time
from db import next_id
from db import Dict
from transwarp_orm import Model, StringField, BooleanField, FloatField, TextField
from flask import Flask, request, render_template,flash,redirect,url_for,make_response
from apis import api

login_mess={}
ctx=threading.local()
_RE_MD5 = re.compile(r'^[0-9a-f]{32}$')

class APIError(Exception):
    def __init__(self,name):
        Exception.__init__(self)
        self.name=name
        self.message='API %s error'%(self.name)

class RegisterError(Exception):
    def __init__(self,name):
        Exception.__init__(self)
        self.name=name
        self.message='Register %s error'%(self.name)

class Page(object):
    def __init__(self, item_count, page_index=1, page_size=10):
        self.item_count = item_count
        self.page_size = page_size
        self.page_count = item_count // page_size + (1 if item_count % page_size > 0 else 0)
        print item_count,page_index,self.page_count

        self.page_index = page_index
        self.offset = int(self.page_size) * (int(page_index) - 1)
        self.limit = self.page_size
        self.has_next = self.page_index < self.page_count
        self.has_previous = self.page_index > 1
        self.message={ 'self.item_count': self.item_count ,
                       'self.page_size':self.page_size,
                       'self.page_count':self.page_count,
                       'self.page_index':self.page_index,
                       'self.offset':self.offset,
                       'self.limit':self.limit,
                       'self.has_next':self.has_next,
                       'self.has_previous':self.has_previous,
                     }



def _get_blogs_by_page():
    b=MyModel.Blog()
    total =b.count()
    print 'total',total
    print 'ctx.get_page_index',ctx.get_page_index
    page = Page(total, ctx.get_page_index)
    blogs = b.select_by('create_at ','desc limit %s,%s'%(str(page.offset), str(page.limit)))
    return blogs, page



app = Flask(__name__)
@app.route('/admin',methods=['GET'])
def admin_sign_in_form():

    return render_template('admin-form.html')

@app.route('/admin',methods=['POST'])
def admin_sign_in():

    username = request.form['username']
    password = request.form['password']
    u=MyModel.User(id=username,password=password)
    dict_admin=u.select_one('id',username)
    print dict_admin
    if dict_admin['admin']==1:
        login_mess['logid']=username

        u = MyModel.User()
        b = MyModel.Blog()
        c = MyModel.Comment()
        list_u = u.select()
        list_b = b.select()
        list_c = c.select()
        list_u_str=  []
        list_b_str = []
        list_c_str = []
        for l in list_u:
            list_u_str.append(str(l))
        for b in list_b:
            list_b_str.append(str(b))
        for c in list_c:
            list_c_str.append(str(c))


        return render_template('form.html',message='%s\n\n %s\n\n %s\n\n' % ('\n'.join(list_u_str), '\n'.join(list_b_str), '\n'.join(list_c_str)),username='Admin')





@app.route('/', methods=['GET', 'POST'])
def home():

    user_info=request.cookies.get('user_info')
    user_name=request.cookies.get('user_name')
    homecookie={'user_info':user_info,'user_name':user_name}
    checkresult=parse_signed_cookie(homecookie)
    if checkresult==True:
        b = MyModel.Blog()
        u = MyModel.User()
        list_blogs = b.select()
        dict_usr = u.select_one('id', user_name)
        print 'listblogs:',list_blogs
        return render_template('blogs.html',blogs=list_blogs,user=dict_usr)

@app.route('/login', methods=['GET'])
def log_in_form():
    return render_template('form.html')

@app.route('/login', methods=['POST'])
def log_in():

    username = request.form['username']
    password = request.form['password']
    u=MyModel.User(id=username,password=password)
    dict_usr=u.select_one('id',username)
    print 'dict_usr:',dict_usr
    if dict_usr['password']==password:
        return home(username)
    else:
        return render_template('form.html', message='Bad username or password', username=username)

@app.route('/signup',methods=['GET'])
def sign_up_form():
    return render_template('signup.html')

@app.route('/signup',methods=['POST'])
def sign_up():

    username = request.form['username']
    password = request.form['password']
    email=request.form['email']
    name=request.form['name']
    u = MyModel.User(id=username, password=password,email=email,name=name)
    dict_signup = u.select_one('id', username)
    print dict_signup

    if dict_signup==[]:
        if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', email):
            u.insert_one()
            return render_template('signup-ok.html',username=username)
        if not re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', email):
            flash('please input right Email adress.')
            return redirect(url_for('sign_up_form'))

    else:
        return render_template('form.html',message='You have already signup,please login')



@app.route('/api/users',methods=['GET'])
def api_get_users():
    u=MyModel.User()
    list_usr=u.select()
    for u in list_usr:
        u.password = '******'
    dict_usr=dict(user=list_usr)
    print 'dict_usr:',dict_usr
    r = json.dumps(dict_usr)
    return r

@app.route('/api/blogs',methods=['GET'])
def api_get_blogs():
    b=MyModel.Blog()
    list_blg=b.select()

    dict_blg=dict(user=list_blg)
    print 'dict_usr:',dict_blg
    r = json.dumps(dict_blg)
    return r

@app.route('/api/comments',methods=['GET'])
def api_get_comments():
    c = MyModel.Comment()
    list_cmt = c.select()

    dict_cmt = dict(user=list_cmt)
    print 'dict_usr:', dict_cmt
    r = json.dumps(dict_cmt)
    return r

@app.route('/api/blogs_by_page',methods=['GET'])
def api_get_blogs_bypage():
    return render_template('blogpage_api.html')

@app.route('/api/blogs_by_page',methods=['POST'])
def api_blogs_bypage():
    ctx.get_page_index=request.form['page']
    print 'ctx.get_page_index',ctx.get_page_index
    blogs,page=_get_blogs_by_page()
    print blogs,page
    r=json.dumps({'page':page.message,'blogs':blogs})
    print r
    return r




@app.route('/register',methods=['GET'])
def register_page():
    return render_template('register.html')


@app.route('/register',methods=['POST'])
def register_user():
    max_age = 604800
    ctx.username=request.form['name']
    ctx.useremail=request.form['email']
    ctx.userpassword=request.form['password2']
    print ctx.username,ctx.useremail,ctx.userpassword
    if not ctx.username:
        raise APIError('name')
    if not ctx.useremail or not re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', ctx.useremail):
        raise APIError('email')
    if not ctx.userpassword or not _RE_MD5.match(ctx.userpassword):
        raise APIError('password')
    u=MyModel.User
    user=u.select_one('id',ctx.username)
    if user:
        raise RegisterError('email')
    user = MyModel.User(id=ctx.username, email=ctx.useremail, password=ctx.userpassword,image='http://www.gravatar.com/avatar/%s?d=mm&s=120' % hashlib.md5(ctx.useremail).hexdigest())
    user.insert_one()
    dict_u=u.select_one('id',ctx.username)
    register_js = json.dumps(dict_u)
    ctx.response = make_response(redirect(url_for('home')))
    ctx.response.set_cookie('user_info', ctx.userpassword, max_age=max_age)
    ctx.response.set_cookie('user_name', ctx.username, max_age=max_age)
    return ctx.response

@app.route('/authenticate',methods=['GET'])
def authenticate_page():
    return render_template('login.html')

@app.route('/authenticate',methods=['POST'])
def authenticate():
    ctx.username= request.form['name']
    ctx.useremail = request.form['email']
    ctx.userpassword = request.form['password']
    u=MyModel.User()
    user = u.select_one('id', ctx.username)
    authenticate_js=json.dumps(user)
    print authenticate_js
    if ctx.username is None:
        raise APIError('name')
    elif user.password != ctx.userpassword:
        print 'usp:',user.password
        print 'ctx:',ctx.useremail
        print 'ctx:',ctx.userpassword
        raise APIError('password')
    max_age = 604800
    ctx.response=make_response(redirect(url_for('home')))
    ctx.response.set_cookie('user_info',ctx.userpassword,max_age=max_age)
    ctx.response.set_cookie('user_name',ctx.username,max_age=max_age)

    return ctx.response

@app.route('/get_cookie',methods=['GET'])
def get_cookie():
    user_info = request.cookies.get('user_info')
    return user_info

@app.route('/manage/blogs/creates',methods=['GET'])
def create_blog_page():
    return render_template('manage_blog_edit.html')

@app.route('/manage/blogs/creates',methods=['POST'])
def update_blog_page():
    user_info = request.cookies.get('user_info')
    user_name = request.cookies.get('user_name')
    homecookie = {'user_info': user_info, 'user_name': user_name}
    checkresult = parse_signed_cookie(homecookie)
    if checkresult:
        ctx.blogname=request.form['name']
        ctx.blogsummary=request.form['summary']
        ctx.blogcontent=request.form['content']
        print 'ctx:',ctx.blogname
        u=MyModel.User()
        user=u.select_one('id',user_name)
        b=MyModel.Blog(user_id=user_name,user_name=user['name'],name=ctx.blogname,summary=ctx.blogsummary,content=ctx.blogcontent)
        b.insert_one()
        return  redirect(url_for('home'))
    else:
        return  redirect(url_for('authenticate_page'))

@app.route('/blogs_by_page',methods=['GET'])
def manage_blog_list():
    return render_template('manage_blog_list.html')


def parse_signed_cookie(cookie):
    id=cookie['user_name']
    pw=cookie['user_info']
    if not cookie:
        return False
    elif ctx.userpassword:
        print 'ctx.userpassword:',ctx.userpassword,'cookie:',cookie
        if ctx.userpassword==pw:
            return True
    elif cookie:
        u=MyModel.User()
        user=u.select_one('id',id)
        if user['password']==pw:
            return True





if __name__ == '__main__':
    db.logging.basicConfig(level=db.logging.DEBUG)
    db.create_engine('www-data', 'www-data', 'test')
    app.run()

