from dice import Dice
from board import Board
from player import Player
from time import sleep

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    


class Game:
    SPEED_FRAME = 0.01

    def __init__(self):
        self.players = []
        self.players_dict = {}
        self.board = Board()
        self.current_player = None
        self.winner = None
        # self.colors = ["red"] # ["red", "green", "yellow", "blue"]
        self.colors = ["red", "green", "yellow", "blue"]
        self.dice = Dice()
        self.initilize_players()

    def initilize_players(self):
        for color in self.colors:
            player = Player(color)
            player.initialize_pieces(Board.initial_pieces)
            self.players.append(player)
            self.players_dict[color] = player

    def update_board(self):
        # clear()
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

        General_turno = 0
        while True:
            General_turno += 1
            print("#======================== Turno =======================#")
            print(f"-------------------->  {General_turno}  <---------------------")
            print("#======================================================#")
           
            self.current_player = actual_player
            self.update_board()
            self.dice.roll()
            dice = self.dice
            print("dado: ",dice)
            print("color jugador: ", actual_player.color)
            # self.dice.value = 6
            # piece = actual_player.next_piece_last()
            piece = actual_player.next_piece_first()
            # piece = actual_player.next_piece_random()
            input("Presiona enter para continuar")
            if piece.first_move:
                initial_pos_coord = Board.start_cells[self.current_player.color]
                x_coord, y_coord = initial_pos_coord

                piece.move_to(x_coord, y_coord) # mover dice.value - 1
                
                self.show_next_frame()

                for i in range(self.dice.value - 1):
                    next_move_direction_to = Board.normal_cells[piece.get_coord()]
                    piece.move_in_direction_to[next_move_direction_to]()

                    self.show_next_frame()
                    
                piece.first_move = False
                

            else:
                for i in range(self.dice.value):
                    if piece.get_coord() in Board.special_cells[actual_player.color]:
                        next_move_direction_to = Board.special_cells[actual_player.color][piece.get_coord()]
                    elif piece.get_coord() in Board.normal_cells:
                        next_move_direction_to = Board.normal_cells[piece.get_coord()]
                    else:
                        piece.finished = True
                        break

                    piece.move_in_direction_to[next_move_direction_to]()
                    if piece.get_coord() in Board.end_cells[actual_player.color]:
                        piece.finished = True
                        break

                    self.show_next_frame()

            pieces_same_position = self.check_pieces_same_position(actual_player, piece)
            if pieces_same_position:
                self.send_to_start(pieces_same_position)
                self.show_next_frame()

            if actual_player.has_won():
                self.winner = actual_player
                print("#======================== Turno =======================#")
                print(f"-------------------->  {General_turno}  <---------------------")
                print("#======================================================#")
                print(f"El ganador es {self.winner.color}")
                break
            actual_player = order_players[(order_players.index(actual_player) + 1) % len(order_players)]
            # input("Presiona enter para continuar")

            
    def show_next_frame(self):
        clear()
        self.update_board()
        self.show_board()
        sleep(self.SPEED_FRAME)
        # clear()

    def check_pieces_same_position(self, player, piece):
        return [
            other_piece
            for p in (p for p in self.players if p != player)
            for other_piece in p.pieces
            if other_piece.get_coord() == piece.get_coord()
        ]
    
    def send_to_start(self, pieces):
        for piece in pieces:
            piece.move_to(*piece.initial_pos)
            self.show_next_frame()
            piece.first_move = True
            piece.number_of_moves = 0





