class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print("Pirate stats: ")
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        return self

    def show_health(self):
        print(f"Pirate Health: {self.health}") 
        return self

    def attack ( self , ninja ):
        # ninja.health -= self.strength
        if ninja.health - self.strength < 0:
            ninja.health = 0
        else: 
            ninja.health -= self.strength
        return self
    @staticmethod
    def randomFunction():
        print("it works")



def outsideFunction():
        pass