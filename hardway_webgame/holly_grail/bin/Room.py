from BaseRoom import BaseRoom


class Home(BaseRoom):
    def __init__(self):
        super(Home, self).__init__('home',False)
        self.trainning=False
    def trainning(self):
        self.trainning=True




class School(BaseRoom):
    def __init__(self):
        super(School,self).__init__('school',True)
    def enter_again(self):
        self.othername=raw_input('enter class or corridor  or library')
        if self.othername=='class':
            self.other=Class()
        elif self.othername=='corridor':
            self.other=Corridor()
        elif self.othername=='library':
            self.other=Library()
        else:
            return False


class Class(BaseRoom):
    def __init__(self):
        super(Class,self).__init__('class',False)

class Corridor(BaseRoom):
    def __init__(self):
        super(Corridor,self).__init__('corridor',False)

class Library(BaseRoom):
    def __init__(self):
        super(Library,self).__init__('library',False)

class Arena(BaseRoom):
    def __init__(self):
        super(Arena, self).__init__('arena',True)








