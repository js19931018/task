from nose.tools import *
import StartGame
from Servent import Neru,Drake

def test_chooseservent():
    StartGame.chooseservent('Neru')
    assert_equal(StartGame.Gamedata.myservent.name,'Neru')
def test_timgo():
    StartGame.timego()
    assert_equal(StartGame.Gamedata.gametime,2)
    StartGame.timego()
    StartGame.timego()
    assert_equal(StartGame.Gamedata.gameday,2)
def test_enter():
    StartGame.enter('home')
    assert_equal(StartGame.Gamedata.room.name,'home')
    assert_equal(StartGame.Gamedata.room.entered,True)
    StartGame.enter('school')
    assert_equal(StartGame.Gamedata.room.name,'school')
    assert_equal(StartGame.Gamedata.room.entered,True)
    assert_equal(StartGame.Gamedata.room.other.name,'corridor')
    assert_equal(StartGame.Gamedata.room.other.entered,True)
def test_battle():
   StartGame.Gamedata.myservent=Neru()
   StartGame.Gamedata.enemy=Drake()
   StartGame.battle('aaaaaa')
   assert_equal(StartGame.Gamedata.myservent.nowhp,50)
   assert_equal(StartGame.Gamedata.enemy.nowhp,0)
def test_rest():
    StartGame.Gamedata.myservent=Neru()
    StartGame.Gamedata.myservent.nowhp=25
    StartGame.rest()
    assert_equal(StartGame.Gamedata.myservent.nowhp,50)

if __name__ == '__main__':
    StartGame.init_test()
    test_rest()