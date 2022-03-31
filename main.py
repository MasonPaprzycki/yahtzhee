import random
playerOne = []
playerTwo = []
for i in range(5):
    playerOne.append(random.randint(1, 6))
    playerTwo.append(random.randint(1, 6))


def yahtzee():
    print("Welcome to Yahtzee, the game were you role 5 dice with the hope to make a set.\n"
         "e.g player one roles, 5,2,4,1,3./n"
         "player one wants to keep the number 2./n"
         "player one would than type 2 to keep the number they want.")

def player(player1):
    if player1:
     player = "one"
    else:
     player = "two"
    return player
print(f"{player} rolled {playerOne}" )








