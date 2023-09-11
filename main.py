from components.game import Game
from util.clear_console import clear

<<<<<<< HEAD
def ask_number_of_players():
    try:
        number_of_players = int(input("Number of players: "))
        if number_of_players < 2 or number_of_players > 4:
            raise ValueError
        return number_of_players
    except ValueError:
        print("Invalid number of players")
        return ask_number_of_players()

if __name__ == "__main__":
    # Techine for the game, which piece to move next
    type_of_plays = ["last", "first", "random"]
    type_of_play = type_of_plays[0]

    clear()
    number_of_players = ask_number_of_players()
    speed_frame = 0.25

    game = Game(number_of_players, type_of_play, speed_frame)
    game.start()
=======
while True:
    try:
        game = Game(input("Cuantos jugadores: "))
        break
    except ValueError as e:
        print(e)
game.start()
>>>>>>> 83aa27e1e6898c54e70135d03c6b7b9648bfb596
