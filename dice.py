import random


class Dice:
    def __init__(self):
        self.value = None

    def roll(self) -> int:
        """
        Retorna un valor aleatorio ente 1 y 6
        """
        self.value = random.randint(1, 6)
        return self.value

    def __str__(self):
        """
        Retorna una representacion grafica del dado
        """
        return f"🎲 {self.value}"
