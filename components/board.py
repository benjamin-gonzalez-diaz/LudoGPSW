from setup.initial_pieces import initial_pieces
from setup.cell import normal_cells, special_cells, start_cells, end_cells
# from setup.board_ui import board
from setup.board_ui_2 import board

class Board:
    initial_pieces = initial_pieces
    normal_cells = normal_cells
    special_cells = special_cells
    start_cells = start_cells
    end_cells = end_cells

    def __init__(self):
        self.board = board
        self.static_board = board

    # def replace_at_index(self, original_str, index, replacement):
    #     return original_str[:index] + replacement + original_str[index + 1:]

    # def fill_board(self, tokens):
    #     self.board = self.static_board[:]  # Asegúrate de iniciar con un tablero limpio
    #     for token in tokens:
    #         x = token[0]
    #         y = token[1]
    #         color = token[2]
    #         self.board = self.replace_at_index(self.board, 16 * y + x + 1, color)
    #     return self.board

    def fill_board(self, tokens):
        self.board = self.deep_copy_matrix(self.static_board)
        for token in tokens:
            x = token[0]
            y = token[1]
            color = token[2]
            self.board[y][x] = color
    
    def show_board(self):
        for row in self.board:
            row = " ".join(row)
            print(row)

    def deep_copy_matrix(self, matrix):
        return [row[:] for row in matrix]

    
    # def string_to_matrix(self, string):
    #     return [list(row) for row in string.strip().split('\n')]

    # def show_board(matrix):
    #     for row in matrix:
    #         row = "".join(row)
    #         print(row)



