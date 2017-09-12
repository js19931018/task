import web
import StartGame
urls = (
'/game', 'GameEngine',
'/', 'Index',
)
app = web.application(urls, globals())
# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store,initializer={'room': None,'time':None,'severnt':None,'hp':None,'enemy':None})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
# this is used to "setup" the session with starting values

        StartGame.init()
        session.room =StartGame.Gamedata.room
        web.seeother("/game")

class GameEngine():
    def GET(self):
        room=StartGame.Gamedata.room
        day=StartGame.Gamedata.gameday
        time=StartGame.Gamedata.gametime
        servent=StartGame.Gamedata.myservent
        enemy=StartGame.Gamedata.enemy



