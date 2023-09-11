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


emoji = {
    "red": {
        1: f"{RED}1{WHITE}",
        2: f"{RED}2{WHITE}",
        3: f"{RED}3{WHITE}",
        4: f"{RED}4{WHITE}",
    },
    "green": {
        1: f"{GREEN}1{WHITE}",
        2: f"{GREEN}2{WHITE}",
        3: f"{GREEN}3{WHITE}",
        4: f"{GREEN}4{WHITE}",
    },
    "yellow": {
        1: f"{YELLOW}1{WHITE}",
        2: f"{YELLOW}2{WHITE}",
        3: f"{YELLOW}3{WHITE}",
        4: f"{YELLOW}4{WHITE}",
    },
    "blue": {
        1: f"{BLUE}1{WHITE}",
        2: f"{BLUE}2{WHITE}",
        3: f"{BLUE}3{WHITE}",
        4: f"{BLUE}4{WHITE}",
    }
}