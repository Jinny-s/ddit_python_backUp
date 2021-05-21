class Gaia:
    def __init__(self):
        self.flag_life = False
    
    def birth(self):
        self.flag_life = True

class JindoDog(Gaia):
    def __init__(self):
        super().__init__()
        self.power_bark = 0
        
    def train(self):
        self.power_bark += 1
        
class SokchoBird(Gaia):
    def __init__(self):
        super().__init__()
        self.flag_fly = False
        
    def practice(self):
        self.flag_fly = True

class GaeSae(JindoDog, SokchoBird):
    def __init__(self):
        JindoDog.__init__(self)
        SokchoBird.__init__(self)

gaesae = GaeSae()
print(gaesae.flag_life, gaesae.power_bark, gaesae.flag_fly)

gaesae.birth()
gaesae.train()
gaesae.practice()
print(gaesae.flag_life, gaesae.power_bark, gaesae.flag_fly)
