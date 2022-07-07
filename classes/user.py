import pirate
import ninja

# class User:

#     def __init__(self, name, strength, speed, health):
#         self.name = name 
#         self.strength = strength 
#         self.speed = speed
#         self.health = health

#     def show_stats( self ):
#         print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

#     def attack ( self , ninja ):
#         ninja.health -= self.strength
#         return self


# character_a = User('Pirate', 15, 3, 100)
# character_b = User('Ninja', 10, 5, 100)

# character_a.show_stats()
# character_b.show_stats()
# character_a.attack(character_b)
# character_b.show_stats()


myPirate = pirate.Pirate("madhav")

myPirate.show_stats()

myNinja = ninja.Ninja("Mert")

myNinja.show_stats()




print("Welcome to the game")

player1Input = input("Choose your player: Ninja or Pirate? For ninja type 'n' for pirate type 'p'  ")


while player1Input != "p" or player1Input != "n":
    if player1Input == "n" or player1Input == "p":
        break
    player1Input = input("Invalid input please put 'n' or 'p'!")
        

if player1Input == "n":
    player1 = myNinja
    player2 = myPirate
    print("player 1 is ninja player 2 is pirate")


elif player1Input == "p":
    player1 = myPirate
    player2 = myNinja
    print("player 1 is pirate and player 2 is ninja")



player1.show_stats()
player2.show_stats()


while player1.health > 0 and player2.health>0 :
    player1.attack(player2)
    player2.show_health()
    player2.attack(player1)
    player1.show_health()


if player1.health <= 0 and player2.health>= 0:
    print("Player 2 wins!")
else: 
    print("Player 1 wins!")

