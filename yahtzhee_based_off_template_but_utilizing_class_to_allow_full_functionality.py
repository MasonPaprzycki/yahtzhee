import random
import operator


class Player:
    def __init__(self, player):
        self.player = player
        self.points = 0
        self.roll = []
        for i in range(5):
            self.roll.append(random.randint(1, 6))

    def reroll(self, reroll):
        try:
            reroll.split(reroll.join(i for i in reroll if i.isdigit()))
            reroll = [int(float(x)) for x in reroll]
            for a in range(len(reroll)):
                self.roll[(reroll[a]) - 1] = random.randint(1, 6)
            print(self.roll)
        except ValueError:
            pass

    def score_points(self, point_method):
        if point_method.isnumeric():
            point_method = int(point_method)
            in_range = self.roll.count(point_method)
            for i in range(in_range):
                self.points += point_method
        elif point_method == 'yahtzee':
            valid = True
            for i in range(1, 6):
                if not self.roll[0] == self.roll[i]:
                    valid = False
            if valid:
                self.points += 50
            else:
                pass
        elif point_method == 'straight':
            valid = True
            for i in range(1, 6):
                if not self.roll[i] > self.roll[i - 1]:
                    valid = False
            if valid:
                self.points += 40
            else:
                pass
        elif point_method == 'chance':
            for i in range(5):
                self.points += self.roll[i]
        if bool(point_method):
            pass
        else:
            print('invalid point method ')


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

player1 = Player('player one')
player2 = Player('player two')
player_bool = True


def player(player_bool):
    if player_bool:
        return player1
    else:
        return player2


def yahtzhee(player_bool):
    print(f'{player(player_bool).player} your roll is {player(player_bool).roll} ')
    reroll = input(f'{player(player_bool).player} what would you like ro reroll? If you dont want to reroll anything \n'
                   f'type nothing and press enter. reroll:  ')
    player(player_bool).reroll(reroll)
    point_meth = input(f'{player(player_bool).player} what method would you like to use to score your point? \n'
                       f'if you want to score by number type it like "1" otherwise type by keyword. \n'
                       f'the keywords are "yahtzhee", "straight", and "chance".  If you dont want to reroll anything \n'
                       f'type nothing and press enter. point method: ')
    player(player_bool).score_points(point_meth)
    print(f'{player(player_bool).player} you scored {str(player(player_bool).points)} points')
    player_bool = operator.not_(player_bool)
    if player1.points > 0 and player2.points > 0:
        if player1.points > player2.points:
            print('player one wins')
        elif player2.points > player1.points:
            print('player two wins')
        else:
            print('tie')
    else:
        yahtzhee(player_bool)


yahtzhee(player_bool)
