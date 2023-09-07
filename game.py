from dice import Dice
from board import Board
from player import Player
from time import sleep
from logger import Logger
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    

class Game:
    SPEED_FRAME = 0.2

    def __init__(self, type_of_play="last"):
        self.players = []
        self.players_dict = {}

        self.dice = Dice()
        self.board = Board()

        self.logger = Logger("log.txt")
        self.logger.clear()

        self.initilize_players(type_of_play)

    def initilize_players(self, type_of_play):
        colors = ["red", "green", "yellow", "blue"]
        for color in colors:
            player = Player(color, type_of_play)
            player.initialize_pieces(Board.initial_pieces)
            self.players.append(player)
            self.players_dict[color] = player

    def update_board(self):
        tokens = []
        for player in self.players:
            for piece in player.pieces:
                tokens.append((piece.x, piece.y, piece.emoji))

        self.board.fill_board(tokens)

    def show_board(self):
        print(self.board.board)

    def get_order_player(self):
        rolls = list(map(lambda player: (player, self.dice.roll()), self.players))
        
        while True:
            rolls.sort(key=lambda x: x[1], reverse=True)
            
            highest_roll = rolls[0][1]
            tied_players = [roll for roll in rolls if roll[1] == highest_roll]
            
            if len(tied_players) == 1:
                return [roll[0] for roll in rolls]
            
            for index, (player, roll) in enumerate(rolls):
                if roll == highest_roll:
                    rolls[index] = (player, self.dice.roll())

    def start(self):
        order_players = self.get_order_player()
        current_player = order_players[0]
        self.show_next_frame()
        sleep(2)

        while True:
            self.dice.roll()

            piece = current_player.next_piece_last(self.dice)

            if piece is None:
                self.show_next_frame()
                current_player = order_players[(order_players.index(current_player) + 1) % len(order_players)]
                continue

            if piece not in current_player.pieces_in_board:
                piece.is_in_board = True
                current_player.pieces_in_board.append(piece)

            if piece.first_move:
                piece.first_move = False

                initial_pos_coord = Board.start_cells[current_player.color]
                x_coord, y_coord = initial_pos_coord

                piece.move_to(x_coord, y_coord) 
                
                self.show_next_frame()

                for _ in range(self.dice.value - 1):
                    next_move_direction_to = Board.normal_cells[piece.get_coord()]
                    piece.move_in_direction_to[next_move_direction_to]()
                    self.show_next_frame()
                
            else:
                piece.first_move = False
                for _ in range(self.dice.value):

                    if piece.get_coord() in Board.special_cells[current_player.color]:
                        next_move_direction_to = Board.special_cells[current_player.color][piece.get_coord()]

                    elif piece.get_coord() in Board.normal_cells:
                        next_move_direction_to = Board.normal_cells[piece.get_coord()]

                    elif piece.get_coord() == Board.end_cells[current_player.color]:
                        piece.finished = True
                        for p in piece.rest_of_kinged_pieces:
                            p.finished = True
                        self.logger.log(f"La pieza {piece} ha terminado y las piezas {piece.rest_of_kinged_pieces} tambien")
                        break

                    elif piece.get_coord() in Board.initial_pieces[current_player.color]["positions"]:
                        raise Exception("La pieza esta en la posición inicial, pero no es la primera jugada y no deberia estar en el tablero")
                    
                    else:
                        raise Exception("La pieza no esta en el tablero ni en la posición inicial")

                    piece.move_in_direction_to[next_move_direction_to]()
                    piece.move_other_kigned_pieces()

                    self.show_next_frame()

            pieces_same_position = self.check_pieces_same_position(piece)

            if pieces_same_position:
                same_color_pieces = [p for p in pieces_same_position if p.color == piece.color]
                different_color_pieces = [p for p in pieces_same_position if p.color != piece.color]

                if same_color_pieces:
                    piece.king(same_color_pieces)
                    for p in same_color_pieces:
                        p.king([piece] + [x for x in same_color_pieces if x != p])

                if different_color_pieces:
                    for p in different_color_pieces:
                        self.send_to_start(p)

                self.show_next_frame()
        
            if current_player.has_won():
                print(f"El ganador es {self.winner.color}")
                break

            current_player = order_players[(order_players.index(current_player) + 1) % len(order_players)]

        
    def show_next_frame(self):
        clear()
        self.update_board()
        self.show_board()
        sleep(self.SPEED_FRAME)

    def check_pieces_same_position(self, piece):
        return [
            other_piece
            for p in self.players
            for other_piece in p.pieces
            if other_piece.get_coord() == piece.get_coord() and other_piece != piece
        ]

    def combine_king_groups(self, player, group1, group2):
        if group1 in player.kinged_pieces and group2 in player.kinged_pieces:
            combined_group = group1 + group2
            player.kinged_pieces.remove(group1)
            player.kinged_pieces.remove(group2)
            player.kinged_pieces.append(combined_group)
        
    def send_to_start(self, piece):
        self.logger.log(f"La pieza {piece} fue enviada al inicio")
        piece.move_to(*piece.initial_pos)
        piece.first_move = True
        piece.number_of_moves = 0
        piece.is_king = False
        piece.rest_of_kinged_pieces = []
        piece.is_in_board = False

        player_of_piece = self.get_player_by_color(piece.color)
        player_of_piece.pieces_in_board.remove(piece)

    def get_player_by_color(self, color):
        return self.players_dict[color]