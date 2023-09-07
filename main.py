from game import Game



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
    type_of_play = type_of_plays[1]

    number_of_players = ask_number_of_players()

    game = Game(number_of_players, type_of_play)
    game.start()
