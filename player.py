from piece import Piece
from random import choice


class Player:

    def __init__(self, color):
        self.color = color
        self.pieces = []
        self.kinged_pieces = []

    def initialize_pieces(self, initial_pieces) -> None:
        """
        Inicializa las fichas del jugador
        """
        for piece in initial_pieces[self.color]["positions"]:
            self.pieces.append(
                Piece(piece[0], piece[1], self.color, initial_pieces[self.color]["emoji"]))

    def has_won(self) -> bool:
        """
        Retorna un booleano si esque el jugador ha ganado,
        es decir, todas sus fichas se encuentran en la meta
        """
        for piece in self.pieces:
            if not piece.finished:
                return False
        return True

    def next_piece_last(self):
        unfinished_pieces = [
            piece for piece in self.pieces if not piece.finished]
        if not unfinished_pieces:
            return None
        return min(unfinished_pieces, key=lambda piece: piece.number_of_moves)

    def next_piece_first(self):
        unfinished_pieces = [
            piece for piece in self.pieces if not piece.finished]
        if not unfinished_pieces:
            return None
        return max(unfinished_pieces, key=lambda piece: piece.number_of_moves)

    def next_piece_random(self):
        unfinished_pieces = [
            piece for piece in self.pieces if not piece.finished]
        if not unfinished_pieces:
            return None
        return choice(unfinished_pieces)

    def __str__(self):
        return self.color

    def __repr__(self):
        return self.color
