class Animal:
    def __init__(self):
        self.fullness = 0
    
    def eat(self):
        self.fullness += 1
    
    def manddang(self):
        self.fullness = 10
        
class Human(Animal):
    def __init__(self):
        super().__init__()
        self.flag_cook = False
        
    def goHakwon(self):
        self.flag_cook = True

    
hum = Human()
print(hum.fullness, hum.flag_cook)
hum.manddang()
hum.goHakwon()
print(hum.fullness, hum.flag_cook)
