from numpy import random

class Dice:
    special_numbers = [1, 6]
    
    def __init__(self):
        self.value = None

    def roll(self):
        self.value = random.randint(1, 7)
        return self.value

    def __str__(self):
        return f"🎲 {self.value}"