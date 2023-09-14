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

    def next_piece(self, method: int = 0) -> Piece:
        """
        Retorna la siguiente ficha ha jugar, se le puede pasar el metodo a
        ocupar.
        0: la pieza con mayor numero de movimientos
        1: la pieza con menor numero de movimientos
        2: al azar
        """
        unfinished_pieces = [
            piece for piece in self.pieces if not piece.finished]
        if not unfinished_pieces:
            return None
        elif method == 0:
            return max(unfinished_pieces, key=lambda piece: piece.number_of_moves)
        elif method == 1:
            return min(unfinished_pieces, key=lambda piece: piece.number_of_moves)
        elif method == 2:
            return choice(unfinished_pieces)

    def __str__(self):
        return self.color

    def __repr__(self):
        return self.color
