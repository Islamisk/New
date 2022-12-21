class Hero:
    def __init__(self,name,ability):
        self.name = name
        self.ability = ability

class Hero_super(Hero):
    def __str__(self):
        return f"{self.name}, {self.ability}"
    def P(self):
        print(f"{self.name} - hero_super")