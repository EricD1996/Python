class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0
    
    def sleep(self):
        self.energy += 25
        print(self.energy)
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(self.energy, self.health)
        return self
    
    def play(self):
        self.health += 5
        print(self.health)
        return self

    def noise(self):
        print("moo")

