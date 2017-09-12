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
    else:
        print 'You exit this game.'
        os._exit(0)


def timego():
    if Gamedata.gametime==3:
       Gamedata.gameday= Gamedata.gameday + 1
       Gamedata.gametime=1
    else:
       Gamedata.gametime=Gamedata.gametime+1

    if Gamedata.gametime==1:
        print 'Day %s,morning'%str(Gamedata.gameday)
    if Gamedata.gametime==2:
        print 'Day %s,noon'%str(Gamedata.gameday)
    if Gamedata.gametime==3:
        print 'Day %s,night'%str(Gamedata.gameday)


def enter(place):

    time=Gamedata.gametime
    if Gamedata.test==0:
       r=raw_input( "Input a place to go,home,school or arena")
    else:
       r=place

    if not (r=='home' or r=='school' or r=='arena'):
        return False
    else:
        Gamedata.room=input_dict[r]
        room=Gamedata.room
        room.enter()

        if r=='school':
            if Gamedata.test==0:
                while room.enter_again()==False:
                    print 'Please input correctly.'
                room.other.enter()

            else:
                room.other=Corridor()
                room.othername='corridor'
                room.other.enter()

            if room.othername=='library':
                    get_information()
            else:
                pass
            if room.othername=='corridor'and time==3:
                    get_dream()
            else:
                pass

        elif r=='home':
            train()

        else:
            pass



    if room.adventrue==False and Gamedata.test==0:
        r_r=raw_input('have a rest? Y/N')
        if r_r=='y':
            if room.have_a_rest():
                rest()
    else:
        pass

    if Gamedata.test==0:
        ipt=raw_input('depart %s? y/n')%Gamedata.room.name
    else:
        ipt='n'
    if ipt=='y':
        room.departed()

    else:
        pass

def get_dream():
    print 'You look at deep blue sky on corridor,and fall sleep .'
    print 'You have a dream about your servent %s,and know his nobelphantasm '%Gamedata.myservent.name
    print '"%s",you can input it as order at fight,only 2 times,remember it.\n'%Gamedata.myservent.nobelphantasm

def get_information():
    print 'you check a lot of books,and found some data of your enemy %s'%Gamedata.enemy.name
    print '%s\n'%information['%s'%Gamedata.enemy.name]

def train():
    MyServent=Gamedata.myservent
    print 'You trained your servent'
    MyServent.atk = MyServent.atk + MyServent.atk_add
    MyServent.hp = MyServent.hp + MyServent.hp_add
    MyServent.damage=MyServent.damage+MyServent.damage_add
    print 'Now you servent hp:%s, atk:%s nobelphantasm:%s' % (str(MyServent.hp), str(MyServent.atk),str(MyServent.damage))


def rest():
    MyServent=Gamedata.myservent
    MyServent.recover()
    print 'Life is recoverd,now %s'%MyServent.nowhp

def battle(testorder):
    MyServent = Gamedata.myservent
    enemy=Gamedata.enemy
    print ('Input 6 orders,b represents break, against defence,has a 2*atk damage,\n'
           'a represents attack,against break,has 1*atk damage\n'
           'd represents defence, against attack,has no damage\n'
           'you can input such as "abdabd" ')
    while True:
        if Gamedata.test==0:
            orders=raw_input()
        else:
            orders=testorder
        if orders==MyServent.nobelphantasm and MyServent.left>=0:
            print 'You successfully use nobelphantasm,and get %s points damage'%str(MyServent.damage)
            enemy.nowhp=enemy.nowhp-MyServent.damage
            MyServent.left=MyServent-1
            print ' %s hp:%s,%s,hp:%s' % (MyServent.name, str(MyServent.nowhp), enemy.name, str(enemy.nowhp))
        if len(orders)==6 and orders_char(orders):
            ordersenemy=enemy.order
            rst=judge(orders,ordersenemy)
            if rst=='win':
               return 'win'
        else:
            print 'Please input right orders'

def orders_char(orders):
    for i in orders:
        if not(i=='a' or i=='b' or i=='d'):
            return False
        else:
            return True

def judge(orders,ordersenemy):
    MyServent=Gamedata.myservent
    enemy=Gamedata.enemy
    for i in range(6):
        r=orders[i]+ordersenemy[i]
        result=input_dict_judge[r]
        if result[0]== 'win':
            you_damage=int(damage_rate[orders[i]])*int(MyServent.atk)
            print 'You successfully %s %s,and got %s points damage'%(shortfor[orders[i]],enemy.name,str(you_damage))
            enemy.nowhp=enemy.nowhp-you_damage
            if judge_death(enemy.nowhp)=='defeated':
                print 'You defeat %s'%enemy.name
                return 'win'



        if result[1]=='win':
            enemy_damage=int(damage_rate[ordersenemy[i]])*int(enemy.atk)
            print "%s %s you successfully,cause %s points damage"%(enemy.name,shortfor[ordersenemy[i]],str(enemy_damage))
            MyServent.nowhp=MyServent.nowhp-enemy_damage
            if judge_death(enemy.nowhp)=='defeated':
                print 'You have benn defeated'
                os._exit(0)

        print ' %s hp:%s,%s,hp:%s'%(MyServent.name,str(MyServent.nowhp),enemy.name,str(enemy.nowhp))


def judge_death(nowhp):
    if nowhp<=0:
        Gamedata.enemy.nowhp=0
        return 'defeated'

def change_enemy(name):
    Gamedata.enemy=input_dict_servent[name]()




if __name__ == '__main__':

    start_game()























