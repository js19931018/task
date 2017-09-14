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
tm_corridor=Corridor()
input_dict={'arena':tm_arena,'home':tm_home,'school':tm_school,'library':tm_library,'class':tm_class,'corridor':tm_corridor}
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





def init():

    Gamedata.gameday=2
    Gamedata.gametime=3
    Gamedata.myservent=Neru()
    Gamedata.enemy=Robinhood()
    Gamedata.test=0
    Gamedata.room=tm_class
    Gamedata.battle=False
    Gamedata.enemydefeat=False
    print 'inited'
    print Gamedata.enemy.name
    print Gamedata.myservent.name
    print Gamedata.battle


def init_test():
    Gamedata.gameday = 1
    Gamedata.gametime = 1
    Gamedata.myservent = Neru()
    Gamedata.enemy = Robinhood()
    Gamedata.test = 1
    Gamedata.room=None




def chooseservent(name):




    ser_inpt=name
    if ser_inpt=='Neru' or ser_inpt=='Robinhood' or ser_inpt=='Drake':

       Gamedata.myservent=input_dict_servent[ser_inpt]
       return 'You choose %s as a servent' %name
    else:
       return 'input a right name.'



def timego():
    if Gamedata.room.entered==False:
        return 'No need to depart'
    Gamedata.room.departed()

    if Gamedata.gametime==3:
        Gamedata.gameday= Gamedata.gameday + 1
        Gamedata.gametime=1
    else:
        Gamedata.gametime=Gamedata.gametime + 1

    if Gamedata.gametime==1:
        return 'Depart %s,Day %s,morning'%(Gamedata.room.name,Gamedata.gameday)
    if Gamedata.gametime==2:
        return 'Depart %s,Day %s,noon'%(Gamedata.room.name,Gamedata.gameday)
    if Gamedata.gametime==3:
        return 'Depart %s,Day %s,night'%(Gamedata.room.name,Gamedata.gameday)


def enter(place):



    r=place

    if not (r=='home' or r=='school' or r=='arena'or r=='corridor'or r=='library'or r=='class'):
        return ['Please input a right place',None]
    else:
        Gamedata.room=input_dict[r]
        room=Gamedata.room
        room.enter()
        if r=='school':

            return 'you have entered school'


        elif r=='home':
            trainresult = train()
            return  'you have entered home \n %s'%trainresult


        elif r=='arena':
            return 'you have entered arena'

        elif r=='library':
            info=get_information()
            return 'you have entered library\n%s'%info

        elif r=='class':
            return 'you have entered class'

        elif r=='corridor':
            dream=get_dream()
            return 'you have entered corridor\n%s'%dream

        else:
            pass








def get_dream():
    return 'You look at deep blue sky on corridor,and fall sleep .\nYou have a dream about your servent %s,and know his nobelphantasm "%s",you can input it as order at fight,only 2 times,remember it.'%(Gamedata.myservent.name ,Gamedata.myservent.nobelphantasm)

def get_information():
    name=Gamedata.enemy.name
    return 'you check a lot of books,and found some data of your enemy %s\n%s\n'%(name,information['%s'%name])

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
    if Gamedata.battle==False:
        Gamedata.battle=True

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
                Gamedata.battle=False
                Gamedata.enemydefeat=True
                return 'win'



        if result[1]=='win':
            enemy_damage=int(damage_rate[ordersenemy[i]])*int(enemy.atk)
            templist.append( "%s %s you successfully,cause %s points damage"%(enemy.name,shortfor[ordersenemy[i]],str(enemy_damage)))
            MyServent.nowhp=MyServent.nowhp-enemy_damage
            if judge_death(MyServent.nowhp)=='defeated':
                Gamedata.battle=False
                return 'You have been defeated'


        templist.append( ' %s hp:%s,%s,hp:%s'%(MyServent.name,str(MyServent.nowhp),enemy.name,str(enemy.nowhp)))

    return templist

def judge_death(nowhp):
    if nowhp<=0:
        Gamedata.enemy.nowhp=0
        return 'defeated'

def change_enemy(name):
    print name
    Gamedata.enemy=input_dict_servent[name].name
    return 'Great,you have new enemy %s'%Gamedata.enemy



























