class Piece:

    def __init__(self, x, y, color, emoji):
        self.x = x
        self.y = y
        self.color = color
        self.emoji = emoji
        self.first_move = True
        self.finished = False
        self.number_of_moves = 0
        self.initial_pos = (x, y)

        self.move_in_direction_to = {
            "up": self.move_up,
            "down": self.move_down,
            "left": self.move_left,
            "right": self.move_right,
            "up-left": self.move_up_left,
            "up-right": self.move_up_right,
            "down-left": self.move_down_left,
            "down-right": self.move_down_right,    
        }
    
    def __str__(self):
        return f"({self.x}, {self.y}) {self.color}"

    def __repr__(self):
        return f"({self.x}, {self.y}) {self.color}"
    
    def move_up(self):
        self.move_to(self.x, self.y - 1)

    def move_down(self):
        self.move_to(self.x, self.y + 1)

    def move_left(self):
        self.move_to(self.x - 1, self.y)

    def move_right(self):
        self.move_to(self.x + 1, self.y)

    def move_up_left(self):
        self.move_to(self.x - 1, self.y - 1)

    def move_up_right(self):
        self.move_to(self.x + 1, self.y - 1)

    def move_down_left(self):
        self.move_to(self.x - 1, self.y + 1)

    def move_down_right(self):
        self.move_to(self.x + 1, self.y + 1)

    def move_to(self, x, y):
        self.x = x
        self.y = y
        self.number_of_moves += 1

    def get_coord(self):
        return (self.x, self.y)
    