import web
import holly_grail
web.config.debug = False
urls = ('/count', 'count',
        '/reset', 'reset')

app = web.application(urls, globals())
store = web.session.DiskStore('sessions')
session = web.session.Session(app, store, initializer={'count': 0})

render = web.template.render('templates/',base="layout")

class count:
    def GET(self):
        session.count += 1
        return str(session.count)

class reset:
    def GET(self):
        session.kill()
        return ""
#class Index(object):
#    def GET(self):
 #       return render.hello_form()

#    def POST(self):
 #       form = web.input(name="Nobody", greet="Hello")

 #       greeting = "%s, %s" % (form.greet, form.name)
 #       return render.index(greeting=greeting)
if __name__ == '__main__':
    app.run()