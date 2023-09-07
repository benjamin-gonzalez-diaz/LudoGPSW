from game import Game

while True:
    try:
        game = Game(input("Cuantos jugadores: "))
        break
    except ValueError as e:
        print(e)
game.start()
