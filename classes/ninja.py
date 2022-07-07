class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print("Ninja stats: ")
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        return self 

    def show_health(self):
        
        print(f"Ninja Health: {self.health}")
        return self 

    def attack( self , pirate ):

        if pirate.health - self.strength < 0:
            pirate.health = 0
        else: 
            pirate.health -= self.strength
        return self