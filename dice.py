from numpy import random

class Dice:

    def __init__(self):
        self.value = None

    def roll(self):
        self.value = random.randint(1, 7)
        return self.value

    def __str__(self):
        return f"🎲 {self.value}"
    
    def can_repeat(self):
        return self.value in [1, 6]