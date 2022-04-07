import random
import operator
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
        player_var = "one"
    else:
        player_var = "two"
    return player_var


def yahtzee(player_one_roll, player_two_roll, player_bool):
    print(f"player one your roll is {player_one_roll}")
    replace = input(f"player {player(player_bool)} what would you like to re roll?")
    replace = ''.join(filter(str.isdigit, replace))
    try:
        replace.split(replace.join(i for i in replace if i.isdigit()))
        replace = [int(float(x)) for x in replace]
        for a in range(len(replace)):
            locals()[f"player_{player(player_bool)}_roll"][(replace[a]) - 1] = random.randint(1, 6)
        print(locals()[f"player_{player(player_bool)}_roll"])
    except ValueError:
        pass
    point_method = "what method would you like to use to score your point "
    player_bool = operator.not_(player_bool)

yahtzee(player_one_roll, player_two_roll, player_bool=True)

