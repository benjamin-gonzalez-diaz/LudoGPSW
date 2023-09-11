from initial_pieces import initial_pieces
from cell import normal_cells, special_cells, start_cells, end_cells
from board_ui import board


class Board:
    initial_pieces = initial_pieces
    normal_cells = normal_cells
    special_cells = special_cells
    start_cells = start_cells
    end_cells = end_cells

    def __init__(self):
        self.board = board
        self.static_board = board

    def replace_at_index(self, original_str, index, replacement) -> str:
        """
        Retorna un str del tablero con la posicion de una ficha actualizada
        """
        return original_str[:index] + replacement + original_str[index + 1:]

    def fill_board(self, tokens) -> None:
        """
        Actualiza el tablero con las posiciones de las fichas actuales
        """
        self.board = self.static_board[:]  # Asegúrate de iniciar con un tablero limpio
        for token in tokens:
            x = token[0]
            y = token[1]
            color = token[2]
            self.board = self.replace_at_index(
                self.board, 16 * y + x + 1, color)

    def __str__(self,):
        """
        Retorna una representacion grafica del tablero actual
        """
        return self.board
