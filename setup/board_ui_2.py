# Definición de los colores
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
WHITE = "\033[97m"

char = "#"
r = f"{RED}{char}{WHITE}"
g = f"{GREEN}{char}{WHITE}"
y = f"{YELLOW}{char}{WHITE}"
b = f"{BLUE}{char}{WHITE}"
w = f"{WHITE}{char}{WHITE}"
v = " "

board = [
    [r,r,r,r,r,r,w,w,w,g,g,g,g,g,g],
    [r,w,w,w,w,r,w,g,g,g,w,w,w,w,g],
    [r,w,w,w,w,r,w,g,w,g,w,w,w,w,g],
    [r,w,w,w,w,r,w,g,w,g,w,w,w,w,g],
    [r,w,w,w,w,r,w,g,w,g,w,w,w,w,g],
    [r,r,r,r,r,r,w,g,w,g,g,g,g,g,g],
    [w,r,w,w,w,w,v,v,v,w,w,w,w,w,w],
    [w,r,r,r,r,r,v,v,v,y,y,y,y,y,w],
    [w,w,w,w,w,w,v,v,v,w,w,w,w,y,w],
    [b,b,b,b,b,b,w,b,w,y,y,y,y,y,y],
    [b,w,w,w,w,b,w,b,w,y,w,w,w,w,y],
    [b,w,w,w,w,b,w,b,w,y,w,w,w,w,y],
    [b,w,w,w,w,b,w,b,w,y,w,w,w,w,y],
    [b,w,w,w,w,b,b,b,w,y,w,w,w,w,y],
    [b,b,b,b,b,b,w,w,w,y,y,y,y,y,y],

]

# for row in board:
#     row = " ".join(row)
#     print(row)
