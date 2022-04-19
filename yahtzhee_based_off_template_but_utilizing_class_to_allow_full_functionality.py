import random
import operator


class Player:
    def __init__(self, roll, points):
        self.roll = roll
        self.points = points

    def roll(self):
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
        if type(point_method) == 'int':
            for point_method in self.roll():
                self.points += point_method
        elif point_method == 'yahtzee':
            valid = True
            for i in range(1, 6):
                if not self.roll()[0] == self.roll()[i]:
                    valid = False
            if valid:
                self.points += 50
            else:
                print('no yahtzhee')
        elif point_method == 'straight':
            valid = True
            for i in range(1, 6):
                if not self.roll()[i] > self.roll()[i - 1]:
                    valid = False
            if valid:
                self.points += 40
            else:
                print('no straight')
        elif point_method == 'chance':
            for i in range(5):
                self.points += self.roll()[i]
        else:
            print('invalid point method ')



