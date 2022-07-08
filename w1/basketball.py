# class  Player:
#     def __init__(self, players):
#         self.name = players["name"]
#         self.age = players['age']
#         self.position = players['position']
#         self.team = players['team']
#     def print_info(self):
#         print(self.name)
#         print(self.age)
#         print(self.position)
#         print(self.team)

players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

# player1 = Player(players[0])
# player1.print_info()


# class Player:
#     def __init__(self, player):
#         self.name = player['name']
#         self.age = player['age']
#         self.position = player['position']
#         self.team = player['team']
#     def print_info(self):
#         print(self.name)
#         print(self.age)
#         print(self.position)
#         print(self.team)
# kevin = {
#     	"name": "Kevin Durant", 
#     	"age":34, 
#     	"position": "small forward", 
#     	"team": "Brooklyn Nets"
# }
# jason = {
#     	"name": "Jason Tatum", 
#     	"age":24, 
#     	"position": "small forward", 
#     	"team": "Boston Celtics"
# }
# kyrie = {
#     	"name": "Kyrie Irving", 
#     	"age":32,
#         "position": "Point Guard", 
#     	"team": "Brooklyn Nets"
# }
    
# # Create your Player instances here!
# player_kevin = Player(kevin)
# player_kevin.print_info()
# # player_jason = ???


new_team = []
for x in range(0, len(players)):
    new_team.append(players[x])
print(new_team)