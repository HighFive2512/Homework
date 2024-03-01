class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def defend(self,damage):
        self.damage = damage
        self.health -= self.damage
        if self.health <= 0:
            self.health = 0
            return f'{self.name} was defeated'

    def heal(self,amount):
        self.amount = amount
        self.health += self.amount

