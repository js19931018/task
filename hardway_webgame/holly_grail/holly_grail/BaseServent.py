

class BaseServent(object):
    def __init__(self,name, atk, hp,  nobelphantasm,damage,atk_add,hp_add,damage_add,order):
        self.atk = atk
        self.hp = hp
        self.nobelphantasm = nobelphantasm
        self.left=3
        self.damage=damage
        self.atk_add=atk_add
        self.hp_add=hp_add
        self.damage_add=damage_add
        self.nowhp=self.hp
        self.order=order
        self.name=name
    def UseNobelphantasm(self):
        self.left=self.left-1

    def recover(self):
        self.nowhp=self.hp


