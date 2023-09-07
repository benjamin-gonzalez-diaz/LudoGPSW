from piece import Piece
from random import choice


class Player:

    def __init__(self, color):
        self.color = color
        self.pieces = []
        self.kinged_pieces = []
        self.pieces_in_board = []
  
    def initialize_pieces(self, initial_pieces):
        for piece in initial_pieces[self.color]["positions"]:
            self.pieces.append(Piece(piece[0], piece[1], self.color, initial_pieces[self.color]["emoji"]))

    def has_won(self):
        for piece in self.pieces:
            if not piece.finished:
                return False
        return True
    
    def next_piece_last(self, dice):
        only_in_board = True if not dice.value in [1, 6] else False
        unfinished_pieces = self.get_not_finished_pieces(only_in_board)

        if not unfinished_pieces:
            return None
        return min(unfinished_pieces, key=lambda piece: piece.number_of_moves)
    
    def next_piece_first(self, dice):
        only_in_board = True if not dice.value in [1, 6] else False
        unfinished_pieces = self.get_not_finished_pieces(only_in_board)

        if not unfinished_pieces:
            return None
        return max(unfinished_pieces, key=lambda piece: piece.number_of_moves)
    
    def next_piece_random(self, dice):
        only_in_board = True if not dice.value in [1, 6] else False
        unfinished_pieces = self.get_not_finished_pieces(only_in_board)

        if not unfinished_pieces:
            return None
        return choice(unfinished_pieces)
    
    def __str__(self):
        return self.color
    
    def __repr__(self):
        return self.color
    
    def get_not_finished_pieces(self, use_only_in_board=False):
        if use_only_in_board:
            unfinished_pieces = [piece for piece in self.pieces_in_board if not piece.finished]
        else:
            unfinished_pieces = [piece for piece in self.pieces if not piece.finished]

        return unfinished_pieces
