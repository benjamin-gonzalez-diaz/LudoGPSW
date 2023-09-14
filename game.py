from dice import Dice
from board import Board
from player import Player
from time import sleep
from piece import Piece

import os


def clear():
    """
    Limpia el terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')


class Game:
    SPEED_FRAME = 0.01

    def __init__(self, number_players: int):
        self.players = []
        self.players_dict = {}
        self.board = Board()
        self.current_player = None
        self.winner = None
        # self.colors = ["red"] # ["red", "green", "yellow", "blue"]
        self.colors = self.__get_player_colors(number_players)
        self.dice = Dice()
        self.initilize_players()
        self.turn = 0

    def __get_player_colors(self, number_players) -> list[str]:
        """
        Retorna una lista de los colores (Jugadores) que van a jugar
        """
        colors = ["red", "green", "yellow", "blue"]
        try:
            number_players = int(number_players)
            if not (2 <= number_players <= 4):
                raise ValueError(
                    "Valor incorrecto, ingrese un numero entre 2 y 4")
            return colors[:number_players]
        except ValueError:
            raise ValueError("Valor incorrecto, ingrese un numero entre 2 y 4")

    def initilize_players(self) -> None:
        """
        Rellena self.players con los jugadores y su color
        """
        for color in self.colors:
            player = Player(color)
            player.initialize_pieces(Board.initial_pieces)
            self.players.append(player)
            self.players_dict[color] = player

    def update_board(self) -> None:
        """
        Actualiza el tablero con las fichas de los jugadores
        """
        tokens = []
        for player in self.players:
            for piece in player.pieces:
                tokens.append((piece.x, piece.y, piece.emoji))

        self.board.fill_board(tokens)

    def get_order_player(self) -> list[Player]:
        """
        El jugador con el dado mas grande comienza el juego, si hay empate,
        los jugadores con empate tiran de nuevo. El juego va desde el que
        empieza y luego sentido del reloj
        """
        tied_players = self.players

        while True:
            player_rolls = list(
                map(lambda player: (player, self.dice.roll()), tied_players))

            for player_roll in player_rolls:
                player: Player = player_roll[0]
                roll: int = player_roll[1]
                print(f"Jugador {player} lanzo {roll}")
                sleep(1)
            sleep(2)
            clear()

            player_rolls.sort(key=lambda x: x[1], reverse=True)

            highest_roll = player_rolls[0][1]
            tied_players = [player_roll[0]
                            for player_roll in player_rolls if player_roll[1] == highest_roll]

            if len(tied_players) == 1:
                player_index = self.players.index(tied_players[0])
                order = self.players[player_index:]+self.players[:player_index]
                print(
                    f"Gano {order[0]}, el orden es {[str(p) for p in order]}")
                sleep(3)
                clear()
                return order

    def increment_turn(self,) -> None:
        """
        Incrementa el turno actual del juego
        """
        self.turn+=1

    def print_turn(self,) -> None:
        """
        Imprime en terminal el turno actual
        """
        print(f"""
#======================== Turno =======================#
#                        {str(self.turn) + (5-len(str(self.turn)))*" "}                         #
#======================================================#
        """)

    def print_roll(self, dice: Dice, player: Player) -> None:
        """
        Imprime en terminal el dado y color de jugador
        """
        print(f"""
Dado: {dice}
Color jugador: {player.color}
        """)

    def wait_enter(self,) -> None:
        """Espera que el jugador aprete enter"""
        input("Presiona enter para continuar")

    def start(self) -> None:
        """
        Procedimiento del juego
        """
        order_players = self.get_order_player()
        actual_player = order_players[0]
        self.show_next_frame()
        sleep(2)

        while True:
            self.increment_turn()
            self.print_turn()
            self.current_player = actual_player
            self.update_board()
            self.dice.roll()
            dice = self.dice
            self.print_roll(dice, actual_player)
            piece = actual_player.next_piece()
            self.wait_enter()
            if piece.first_move:
                initial_pos_coord = Board.start_cells[self.current_player.color]
                x_coord, y_coord = initial_pos_coord

                piece.move_to(x_coord, y_coord)  # mover dice.value - 1

                self.show_next_frame()

                for i in range(self.dice.value - 1):
                    next_move_direction_to = Board.normal_cells[piece.get_coord(
                    )]
                    piece.move_in_direction_to[next_move_direction_to]()

                    self.show_next_frame()

                piece.first_move = False

            else:
                for i in range(self.dice.value):
                    if piece.get_coord() in Board.special_cells[actual_player.color]:
                        next_move_direction_to = Board.special_cells[actual_player.color][piece.get_coord(
                        )]
                    elif piece.get_coord() in Board.normal_cells:
                        next_move_direction_to = Board.normal_cells[piece.get_coord(
                        )]
                    else:
                        piece.finished = True
                        break

                    piece.move_in_direction_to[next_move_direction_to]()
                    if piece.get_coord() in Board.end_cells[actual_player.color]:
                        piece.finished = True
                        break

                    self.show_next_frame()

            pieces_same_position = self.check_pieces_same_position(
                actual_player, piece)
            if pieces_same_position:
                self.send_to_start(pieces_same_position)
                self.show_next_frame()

            if actual_player.has_won():
                self.winner = actual_player
                self.print_turn()
                print(f"El ganador es {self.winner.color}")
                break
            actual_player = order_players[(order_players.index(
                actual_player) + 1) % len(order_players)]
            # input("Presiona enter para continuar")

    def show_next_frame(self) -> None:
        """
        Imprime el tablero en el terminal
        """
        clear()
        self.update_board()
        print(self.board)
        sleep(self.SPEED_FRAME)

    def check_pieces_same_position(self, player: Player, piece: Piece) -> list[Piece]:
        """
        Retorna una lista con las fichas que se encuentren en la posicion de la ficha
        actual, y que no pertenescan al jugador.
        """
        pieces_same_pos: list[Piece] = []

        other_players: list[Player] = [p for p in self.players if p != player]
        for op in other_players:
            op_pieces = op.pieces
            for op_piece in op_pieces:
                if op_piece.get_coord() == piece.get_coord():
                    pieces_same_pos.append(op_piece)

        return pieces_same_pos

    def send_to_start(self, pieces) -> None:
        """
        Resetea una ficha a su estado inicial
        """
        for piece in pieces:
            piece.move_to(*piece.initial_pos)
            self.show_next_frame()
            piece.first_move = True
            piece.number_of_moves = 0
