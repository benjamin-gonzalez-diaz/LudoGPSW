from game import Game

# Techine for the game, which piece to move next
type_of_plays = ["last", "first", "random"]
type_of_play = type_of_plays[2]

game = Game(type_of_play)
game.start()