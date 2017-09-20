class BaseRoomError(Exception):
    def __init__(self,message):
        print message



class BaseRoom(object):
    def __init__(self,name,adventure):
        self.name=name
        self.entered=False
        self.welcome="You have entered %s room,ready."%name
        self.adventrue=adventure
        self.goodbye="You have left the room %s,good luck."%name
    def enter(self):
        self.entered=True
        print self.welcome
    def departed(self):
        self.entered=False
        print self.goodbye
    def have_a_rest(self):
        if self.entered==False:
            raise BaseRoomError('You have not at %s'%self.name)
        elif self.adventrue:
            print '%s is a danger place,cannot rest '
        else:
            return True




