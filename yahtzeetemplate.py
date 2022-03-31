import random

player_one_roll = []
player_two_roll = []
for i in range(5):
    player_one_roll.append(random.randint(1, 6))
    player_two_roll.append(random.randint(1, 6))
print("just type the numbers of the dice you want to re-roll \n"
      "not the numbers that the dice themselves rolled \n"
      "e.g: your dice numbers are 2,5,3,1,4 \n"
      "if you want to change the dice that \n"
      "rolled a five type \"2\" \n"
      "if you want to re-roll multiple dice just type in their numbers \n"
      " it doesn't matter and you don't have to worry about spaces \n"
      " e.g \"2353\" or \"1 3 45 3\" \n"
      "by the way you can only type in 5 numbers \n"
      "because you only have five dice \n"
      "if you enter in something wrong the game will tell you")


def player(player1):
    if player1:
        player = "one"
    else:
        player = "two"
    return player


def yahtzee(player_one_roll, player_two_roll):
    print(f"player one your roll is {player_one_roll}")
    replace = input(f"player {player} what would you like to re roll?")
    replace = replace.split(replace.join(i for i in replace if i.isdigit()))
    for a in range(len(replace)):
        player_one_roll[replace[a]] = random.randint(1, 6)







