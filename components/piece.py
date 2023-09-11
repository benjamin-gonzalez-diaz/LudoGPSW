import pygame.mixer
from util.resource_path import resource_path
pygame.mixer.init()


class Piece:

    def __init__(self, x, y, color, emoji, identifier):
        self.x = x
        self.y = y
        self.color = color
        self.emoji = emoji
        self.first_move = True
        self.finished = False
        self.number_of_moves = 0
        self.initial_pos = (x, y)
        self.is_king = False
        self.rest_of_kinged_pieces = []
        self.is_in_board = False
        self.identifier = identifier

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
        return f"id:{self.identifier} pos:({self.x}, {self.y}) c:{self.color}"

    def __repr__(self):
        return f"id:{self.identifier} pos:({self.x}, {self.y}) c:{self.color}"
    
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
        pygame.mixer.music.load(resource_path(f"sounds/{self.color}.mp3"))
        pygame.mixer.music.play()
        self.x = x
        self.y = y
        self.number_of_moves += 1

    def get_coord(self):
        return (self.x, self.y)
    
    def king(self, pieces_below):
        self.is_king = True

        all_kinged_pieces = set(self.rest_of_kinged_pieces + [self] + pieces_below)

        for piece in all_kinged_pieces:
            piece.is_king = True
            piece.rest_of_kinged_pieces = list(all_kinged_pieces - {piece})

    def move_other_kigned_pieces(self):
        for piece in self.rest_of_kinged_pieces:
            piece.x = self.x
            piece.y = self.y
            piece.number_of_moves += 1

    def update_emoji(self, new_emoji):
        self.emoji = new_emoji

