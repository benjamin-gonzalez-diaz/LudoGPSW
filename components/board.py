from setup.initial_pieces import initial_pieces
from setup.cell import normal_cells, special_cells, start_cells, end_cells
from setup.board_ui import board

class Board:
    initial_pieces = initial_pieces
    normal_cells = normal_cells
    special_cells = special_cells
    start_cells = start_cells
    end_cells = end_cells

    def __init__(self):
        self.board = board
        self.static_board = board

    def replace_at_index(self, original_str, index, replacement):
        return original_str[:index] + replacement + original_str[index + 1:]

    def fill_board(self, tokens):
        self.board = self.static_board[:]  # Asegúrate de iniciar con un tablero limpio
        for token in tokens:
            x = token[0]
            y = token[1]
            color = token[2]
            self.board = self.replace_at_index(self.board, 16 * y + x + 1, color)
        return self.board