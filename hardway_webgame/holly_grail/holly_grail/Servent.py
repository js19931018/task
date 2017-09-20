from BaseServent import BaseServent
class Neru(BaseServent):
    def __init__(self):
        super(Neru, self).__init__('Neru',7,50,'vein of petals',20,4,10,15,'abdabd')
class Robinhood(BaseServent):
    def __init__(self):
        super(Robinhood, self).__init__('Robinhood',30,60,'Yew Bow',30,10,2,10,'aadaad')
class Drake(BaseServent):
    def __init__(self):
        super(Drake,self).__init__('Drake',16,180,'unknown',15,10,10,10,'bbbbbb')

class Gawain(BaseServent):
    def __init__(self):
        super(Gawain,self).__init__('Gawain',35,500,'Gallatin',250,10,10,10,'abdabd')


if __name__ == '__main__':
    neru=Neru()
    print neru.atk