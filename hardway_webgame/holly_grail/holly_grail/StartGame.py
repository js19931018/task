from Room import Home,School,Class,Library,Arena,Corridor
from Servent import Neru,Gawain,Robinhood,Drake
import threading
Gamedata=threading.local()

import os
GameDay=1
Gametime=1

MyServent=Neru()


Enemy=Robinhood()

tm_home=Home()
tm_school=School()
tm_class=Class()
tm_library=Library()
tm_arena=Arena()
input_dict={'arena':tm_arena,'home':tm_home,'school':tm_school,'library':tm_library,'class':tm_class}
input_dict_servent={'Neru':Neru(),'Gawain':Gawain(),'Robinhood':Robinhood(),'Drake':Drake()}
input_dict_judge={'ad':['lose','win'],'ab':['win','lose'],'aa':['win','win'],
                  'ba':['lose','win'],'bb':['win','win'],'bd':['win','lose'],
                  'da':['win','lose'],'db':['lose','win'],'dd':['win','win']


                  }
damage_rate={'a':1,'b':2,'d':0}
shortfor={'a':'attack','b':'break','d':'defence'}
conversation={'hard':'We are nerely defeated!',
              'easy':'Not hard.',
              'get':'we get a important infomation.',
              'rest':'It is late, go home now.',
              'win':'Great,we defeat them.'}

information={'Gawain':'Gawain has no weak points,he is desperately strong,good luck',
             'Robinhood':'He only use attack and defence,he has little hp',
             'Drake':'He only use break,use order such as aaaaaa to attack '}

def start_game():

    init()

    chooseservent('Neru')
    while not(Gamedata.gameday%2==0 and Gamedata.gametime==3):
        while enter('')==False:
            print 'Choose a place.'
        timego()
    print 'you enter in arena now,your enemy is %s'%Gamedata.enemy.name
    tm_arena.entered=True
    result=battle('')
    if result=='win':
        change_enemy('Drake')
    timego()

    while not (Gamedata.gameday % 2 == 0 and Gamedata.gametime == 3):
        while enter('') == False:
            print 'Choose a place.'
        timego()
    print 'you enter in arena now,your enemy is %s'%Gamedata.enemy.name
    tm_arena.entered = True
    result = battle('')
    if result == 'win':
        change_enemy('Drake')
    timego()

    while not (Gamedata.gameday % 2 == 0 and Gamedata.gametime == 3):
        while enter('') == False:
            print 'Choose a place.'
        timego()
    print 'you enter in arena now,your enemy is %s'%Gamedata.enemy.name
    tm_arena.entered = True
    result=battle('')
    if result=='win':
        print 'You defeat all enemys and got holly grail,congratulations!'
        os._exit(0)



def init():
    print 'You will take an adventrue,you can go 3 place in a day.\nEvery 2 day you will in arena to defeat a enemy\n Every place has its use,try it'
    Gamedata.gameday=1
    Gamedata.gametime=1
    Gamedata.myservent=Neru()
    Gamedata.enemy=Robinhood()
    Gamedata.test=0
    Gamedata.room=None
    Gamedata.battle='peace'

def init_test():
    Gamedata.gameday = 1
    Gamedata.gametime = 1
    Gamedata.myservent = Neru()
    Gamedata.enemy = Robinhood()
    Gamedata.test = 1
    Gamedata.room=None




def chooseservent(name):


    print('Select a servent:Neru,Robinhood or Drake,Neru suggested.They fight for you.')

    ser_inpt=name
    if ser_inpt=='Neru' or ser_inpt=='Robinhood' or ser_inpt=='Drake':

       Gamedata.myservent=input_dict_servent[ser_inpt]
       return 'You choose %s as a servent' %name
    else:
        print 'You exit this game.'
        os._exit(0)


def timego(depart):
    if depart=='depart':
        Gamedata.room.depart()
        if Gamedata.gametime==3:
           Gamedata.gameday= Gamedata.gameday + 1
           Gamedata.gametime=1
        else:
           Gamedata.gametime=Gamedata.gametime + 1

        if Gamedata.gametime==1:
            return 'Day %s,morning'%str(Gamedata.gameday)
        if Gamedata.gametime==2:
            return 'Day %s,noon'%str(Gamedata.gameday)
        if Gamedata.gametime==3:
            return 'Day %s,night'%str(Gamedata.gameday)
    else:
        pass


def enter(place):



    r=place

    if not (r=='home' or r=='school' or r=='arena'or r=='corridor'or r=='library'or r=='class'):
        return ['Please input a right place',None]
    else:
        Gamedata.room=input_dict[r]
        room=Gamedata.room
        room.enter()
        if r=='school':
            return ['you have entered school',room]


        elif r=='home':
            return  ['you have entered home',room]


        elif r=='arena':
            return ['you have entered arena',room]

        elif r=='library':
            return ['you have entered library',room]

        elif r=='class':
            return ['you have entered class',room]

        elif r=='corridor':
            return ['you have entered corridor',room]

        else:
            pass








def get_dream():
    return ['You look at deep blue sky on corridor,and fall sleep .' ,'You have a dream about your servent %s,and know his nobelphantasm '%Gamedata.myservent.name ,'"%s",you can input it as order at fight,only 2 times,remember it.'%Gamedata.myservent.nobelphantasm]

def get_information():
    return ['you check a lot of books,and found some data of your enemy %s'%Gamedata.enemy.name,'%s\n'%information['%s'%Gamedata.enemy.name]]

def train():
    MyServent=Gamedata.myservent

    MyServent.atk = MyServent.atk + MyServent.atk_add
    MyServent.hp = MyServent.hp + MyServent.hp_add
    MyServent.damage=MyServent.damage+MyServent.damage_add
    return 'You trained your servant,\nNow you servant hp:%s, atk:%s nobelphantasm:%s' % (str(MyServent.hp), str(MyServent.atk),str(MyServent.damage))


def rest():
    MyServent=Gamedata.myservent
    MyServent.recover()
    return 'Life is recoverd,now %s'%MyServent.nowhp

def battle(orders):
    if Gamedata.battle=='peace':
        Gamedata.battle='fight'

        return 'You are in battle now.\nInput 6 orders,b represents break, against defence,has a 2*atk damage,\na represents attack,against break,has 1*atk damage\nd represents defence, against attack,has no damage\nyou can input such as "abdabd" '

    MyServent = Gamedata.myservent
    enemy=Gamedata.enemy



    if orders==MyServent.nobelphantasm and MyServent.left>=0:

        enemy.nowhp=enemy.nowhp-MyServent.damage
        MyServent.left=MyServent-1
        return ['You successfully use nobelphantasm,and get %s points damage' % str(MyServent.damage) ,' %s hp:%s,%s,hp:%s' % (MyServent.name, str(MyServent.nowhp), enemy.name, str(enemy.nowhp))]
    if len(orders)==6 and orders_char(orders):
        ordersenemy=enemy.order
        rst=judge(orders,ordersenemy)
        if rst=='win':
           return 'win'
        else:
            return rst
    else:
        return 'Please input right orders'

def orders_char(orders):
    for i in orders:
        if not(i=='a' or i=='b' or i=='d'):
            return False
        else:
            return True

def judge(orders,ordersenemy):
    MyServent=Gamedata.myservent
    enemy=Gamedata.enemy
    templist = []
    for i in range(6):

        r=orders[i]+ordersenemy[i]
        result=input_dict_judge[r]
        if result[0]== 'win':
            you_damage=int(damage_rate[orders[i]])*int(MyServent.atk)
            templist.append('You successfully %s %s,and got %s points damage'%(shortfor[orders[i]],enemy.name,str(you_damage)))
            enemy.nowhp=enemy.nowhp-you_damage
            if judge_death(enemy.nowhp)=='defeated':
                print 'You defeat %s'%enemy.name
                return 'win'



        if result[1]=='win':
            enemy_damage=int(damage_rate[ordersenemy[i]])*int(enemy.atk)
            templist.append( "%s %s you successfully,cause %s points damage"%(enemy.name,shortfor[ordersenemy[i]],str(enemy_damage)))
            MyServent.nowhp=MyServent.nowhp-enemy_damage
            if judge_death(enemy.nowhp)=='defeated':
                return 'You have benn defeated'


        templist.append( ' %s hp:%s,%s,hp:%s'%(MyServent.name,str(MyServent.nowhp),enemy.name,str(enemy.nowhp)))

    return templist

def judge_death(nowhp):
    if nowhp<=0:
        Gamedata.enemy.nowhp=0
        return 'defeated'

def change_enemy(name):
    Gamedata.enemy=input_dict_servent[name]()
    return 'Great,you have new enemy %s'%Gamedata.enemy




if __name__ == '__main__':

    start_game()























