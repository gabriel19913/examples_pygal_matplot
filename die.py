from random import randint


class Die():
    '''Class the simulates a dice'''
    def __init__(self, num_sides=6):
        # Method that simulates a dice. The default is a six side dice
        self.num_sides = num_sides

    def roll(self):
        # Method that chose a random number between one and the dice's 
        # number of sides 
        return randint(1, self.num_sides)
