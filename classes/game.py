from ninja import Ninja
from pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

class Game:

    def __init__(self, ninja, pirate):
        self.player1 = None
        self.player2 = None
        self.ninja = ninja
        self.pirate = pirate


    def assignPlayers(self):
        print("Welcome to the game")
        player1Input = input("Choose your player: Ninja or Pirate? For ninja type 'n' for pirate type 'p'  ")
        while player1Input != "p" or player1Input != "n":
            if player1Input == "n" or player1Input == "p":
                break
            player1Input = input("Invalid input please put 'n' or 'p'!")
        

        if player1Input == "n":
            self.player1 = self.ninja
            self.player2 = self.pirate
            print("player 1 is ninja player 2 is pirate")

        elif player1Input == "p":
            self.player1 = self.pirate
            self.player2 = self.ninja
            print("player 1 is pirate and player 2 is ninja")
        return self

    def startBattle(self):
        while self.player1.health > 0 and self.player2.health>0 :
            self.player1.attack(self.player2)
            self.player2.show_health()
            self.player2.attack(self.player1)
            self.player1.show_health()
        return self


    def showWinner(self):
        if self.player1.health <= 0 and self.player2.health>= 0:
            print("Player 2 wins!")
        else: 
            print("Player 1 wins!")
        return self


myGame = Game(michelangelo, jack_sparrow)
myGame.assignPlayers().startBattle().showWinner()




