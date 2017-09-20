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
    session = web.session.Session(app, store,initializer={'room': None,'time':None})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/')

class Index(object):
    def GET(self):
# this is used to "setup" the session with starting values

        web.seeother("/game")

Inputchar={'place':['school','corridor','home','arena','library','class'],
           'sname':['Neru','Gawain','Robinhood','Drake']}
Enemylist=['Gawain','Drake','Neru']
class GameEngine():
    def GET(self):

        StartGame.init()
        return render.game(message='start',room='no room' ,time='0',day='0')

    def POST(self):
        form = web.input()
        self.battlemode=StartGame.Gamedata.battle
        self.action=form.action
        message=self.judge()
        if StartGame.Gamedata.room.entered:
           session.room=StartGame.Gamedata.room.name
        else:
            session.room='no room'
        session.time=StartGame.Gamedata.gametime
        session.day=StartGame.Gamedata.gameday
        return render.game(message=message,room=session.room,time=session.time,day=session.day)


    def choosesevant(self, name):
        return StartGame.chooseservent(name)
    def enter(self, name):
        if StartGame.Gamedata.room.entered==False:
           return StartGame.enter(name)
        else:
           return 'you should depart %s first'%StartGame.Gamedata.room.name
    def changeenemy(self,name):
        if StartGame.Gamedata.enemydefeat==True:
           return StartGame.change_enemy(name)

    def battle(self, orders):
        return StartGame.battle(orders)
    def timego(self):
        return StartGame.timego()
    def judge(self):
        if self.battlemode:
            return str(self.battle(self.action))
        if filter(lambda x: x==self.action, Inputchar['place']  ):
            return self.enter(self.action)
        if self.action=='depart':
            return self.timego()
        if filter(lambda x: x==self.action, Inputchar['sname']  ):
            return self.choosesevant(self.action)
        if self.action=='battle':
            return self.battle('')
        if self.action=='change':
            if StartGame.Gamedata.enemydefeat and Enemylist:
               enemy=Enemylist.pop(0)
               return self.changeenemy(enemy)
            elif not StartGame.Gamedata.enemydefeat:
                return 'Defeat enemy first'
            else:
                return 'You have defeated all'



if __name__ == '__main__':
    app.run()







