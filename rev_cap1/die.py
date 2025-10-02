from random import randint

class Die():
    ''''''
    def __init__(self, num_sides=6):
        ''''''
        self.num_sides = num_sides

    def roll(self):
        ''''''
        result = randint(1, self.num_sides + 1)
        return result
    
    def mult_roll(self, num_roll):
        ''''''
        mult_roll = [self.roll() for _ in range(num_roll)]
        return mult_roll