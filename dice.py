import random


class Dice:
    def __init__(self):
        self.value = None

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value

    def __str__(self):
        return f"🎲 {self.value}"
