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

    def __init__(self):
        self.players = []
        self.players_dict = {}
        self.board = Board()
        self.current_player = None
        self.winner = None
        # self.colors = ["red"] # ["red", "green", "yellow", "blue"]
        self.colors = ["red", "green", "yellow", "blue"]
        self.dice = Dice()

        self.logger = Logger("log.txt")
        self.logger.clear()
        self.initilize_players()

    def initilize_players(self):
        for color in self.colors:
            player = Player(color)
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
        actual_player = order_players[0]
        self.show_next_frame()
        sleep(2)

        while True:

            self.current_player = actual_player
            self.dice.roll()

            piece = actual_player.next_piece_last(self.dice)

            if piece is None:
                self.show_next_frame()
                actual_player = order_players[(order_players.index(actual_player) + 1) % len(order_players)]
                continue

            if piece not in actual_player.pieces_in_board:
                piece.is_in_board = True
                actual_player.pieces_in_board.append(piece)

            if piece.first_move:
                piece.first_move = False

                initial_pos_coord = Board.start_cells[self.current_player.color]
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

                    if piece.get_coord() in Board.special_cells[actual_player.color]:
                        next_move_direction_to = Board.special_cells[actual_player.color][piece.get_coord()]

                    elif piece.get_coord() in Board.normal_cells:
                        next_move_direction_to = Board.normal_cells[piece.get_coord()]

                    elif piece.get_coord() == Board.end_cells[actual_player.color]:
                        piece.finished = True
                        for p in piece.rest_of_kinged_pieces:
                            p.finished = True
                        self.logger.log(f"La pieza {piece} ha terminado y las piezas {piece.rest_of_kinged_pieces} también")
                        break

                    elif piece.get_coord() in Board.initial_pieces[actual_player.color]["positions"]:
                        raise Exception("La pieza está en la posición inicial, pero no es la primera jugada y no deberia estar en el tablero")
                    
                    else:
                        raise Exception("La pieza no está en el tablero ni en la posición inicial")

                    piece.move_in_direction_to[next_move_direction_to]()
                    piece.move_other_kigned_pieces()

                    self.show_next_frame()

            pieces_same_position = self.check_pieces_same_position(actual_player, piece)

            if actual_player.has_won():
                self.winner = actual_player
                break
            
            if pieces_same_position:
                same_color_pieces = [p for p in pieces_same_position if p.color == piece.color]
                different_color_pieces = [p for p in pieces_same_position if p.color != piece.color]

                if same_color_pieces:
                    piece.king(same_color_pieces)
                    for p in same_color_pieces:
                        p.king([piece] + [x for x in same_color_pieces if x != p])

                if different_color_pieces:
                    for p in different_color_pieces:
                        self.send_to_start(p)  # Solo enviamos la pieza que ya estaba en la casilla al inicio.


                self.show_next_frame()
            
            

            actual_player = order_players[(order_players.index(actual_player) + 1) % len(order_players)]

            # print("Jugo el jugador", actual_player.color)
        print(f"El ganador es {self.winner.color}")

    def show_next_frame(self):
        clear()
        self.update_board()
        self.show_board()
        sleep(self.SPEED_FRAME)

    def check_pieces_same_position(self, player, piece):
        return [
            other_piece
            for p in self.players
            for other_piece in p.pieces
            if other_piece.get_coord() == piece.get_coord() and other_piece != piece
        ]

    def try_to_king_piece(self, player, piece):
        pieces_same_position = self.check_pieces_same_position(player, piece)

        if pieces_same_position:
            are_same_color = all(piece.color == piece_same_position.color for piece_same_position in pieces_same_position)
            
            if are_same_color:
                player.kinged_pieces.append(pieces_same_position)
                return True

        return False

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





if __name__ == "__main__":
    game = Game()
    game.start()

