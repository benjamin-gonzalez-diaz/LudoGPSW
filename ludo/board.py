import os
import time


board = """
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛🟥🟥🟥🟥🟥🟥⬜⬜⬜🟩🟩🟩🟩🟩🟩⬛
⬛🟥⬜⬜⬜⬜🟥⬜🟩🟩🟩⬜⬜⬜⬜🟩⬛
⬛🟥⬜🔴🔴⬜🟥⬜🟩⬜🟩⬜🟢🟢⬜🟩⬛
⬛🟥⬜🔴🔴⬜🟥⬜🟩⬜🟩⬜🟢🟢⬜🟩⬛
⬛🟥⬜⬜⬜⬜🟥⬜🟩⬜🟩⬜⬜⬜⬜🟩⬛
⬛🟥🟥🟥🟥🟥🟥⬜🟩⬜🟩🟩🟩🟩🟩🟩⬛
⬛⬜🟥⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬛
⬛⬜🟥🟥🟥🟥🟥⬛⬛⬛🟨🟨🟨🟨🟨⬜⬛
⬛⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜🟨⬜⬛
⬛🟦🟦🟦🟦🟦🟦⬜🟦⬜🟨🟨🟨🟨🟨🟨⬛
⬛🟦⬜⬜⬜⬜🟦⬜🟦⬜🟨⬜⬜⬜⬜🟨⬛
⬛🟦⬜🔵🔵⬜🟦⬜🟦⬜🟨⬜🟡🟡⬜🟨⬛
⬛🟦⬜🔵🔵⬜🟦⬜🟦⬜🟨⬜🟡🟡⬜🟨⬛
⬛🟦⬜⬜⬜⬜🟦🟦🟦⬜🟨⬜⬜⬜⬜🟨⬛
⬛🟦🟦🟦🟦🟦🟦⬜⬜⬜🟨🟨🟨🟨🟨🟨⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
"""


def replace_at_index(original_str, index, replacement):
    return original_str[:index] + replacement + original_str[index + 1:]

def fill_board(tokens, board=board):
    for token in tokens:
        x = token[0]
        y = token[1]
        color = token[2]
        board = replace_at_index(board, 18*y+x+1, color)
    return board

print(fill_board([(7,7,'🔴'), (8,8,'🟡')]))



# function to clear console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


for i in range(10):
    clear()
    print(fill_board([(7,1+i,'🔴'), (8,8,'🟡')]))
    time.sleep(0.5)
