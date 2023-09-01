import random
list_player = []
list_dice = []
list_player_And_dice = []
new_list = []
list_order = []
play = False
# Función para lanzar el dado
def lanzar_dado():
    return random.randint(1, 6)

def generar_lista_jugadores_y_dados(num_jugadores,opt):
    list_player = []
    list_dice = []
    list_player_and_dice = []
    if(opt == 1):
        for i in range(num_jugadores):
            jugador = i + 1
            dado = lanzar_dado()
            list_player.append(jugador)
            list_dice.append(dado)
            list_all = [jugador, dado]
            list_player_and_dice.append(list_all)

    elif(opt == 0):
        for i in (num_jugadores):
            jugador = i 
            dado = lanzar_dado()
            list_player.append(jugador)
            list_dice.append(dado)
            list_all = [jugador, dado]
            list_player_and_dice.append(list_all)

    return list_player_and_dice, list_dice, list_player

def reemplazar_empates(list_dice, list_player_And_dice, list_order, jugadores):
    empates = [i for i in range(7) if list_dice.count(i) > 1]

    for i in empates:
        for j in range(jugadores):
            if list_player_And_dice[j][1] == i:
                print("El jugador", list_player_And_dice[j][0], "vuelve a tirar")
                list_order.append(list_player_And_dice[j][0])

    print("list_order:", list_order)
    list_player2 = list_player_And_dice.copy()

    for i in list_order:
        list_player2 = [player for player in list_player2 if player[0] != i]

    all2 = generar_lista_jugadores_y_dados(list_order, 0)
    new_dice = all2[0]

    for i in range(len(list_player_And_dice)):
        for j in range(len(list_order)):
            if list_player_And_dice[i][0] == list_order[j]:
                list_player_And_dice.remove(list_player_And_dice[i])
                list_player_And_dice.append(new_dice[j])

    return list_player_And_dice

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = 0  # Inicialmente, todos los jugadores están en la casilla de inicio
    
    def avanzar(self, pasos):
        self.posicion += pasos

def jugador_y_dado(jugador, n_dado):
    return [jugador, n_dado]

jugadores = int(input("cantidad de jugadores entre 2-4:         "))
if(jugadores > 4):
    jugadores = 4
if(jugadores < 2):
    jugadores = 2

all = (generar_lista_jugadores_y_dados(jugadores,1))
list_dice = all[1]
list_player_And_dice = all[0]
list_player = all[2]

print("list_dice", list_dice)
for i in range(7):
    if(list_dice.count(i) > 1):
        play = False
        for j in range(jugadores):
            if (list_player_And_dice[j][1] == i):
                print("el jugador ", list_player_And_dice[j][0]," vuelve a tirar")
                list_order.append(list_player_And_dice[j][0])
            else:
                play = True


print(play)
print("list_order: ",list_order)
print("list_player", list_player)
list_player2 = list_player
for i in (list_order):
    list_player2.remove(i)
print("list_player2",list_player2)
all2 = generar_lista_jugadores_y_dados(list_order,0)
print(all2)
new_dice = all2[0]

print("list_dice",list_dice)
print("list_player",list_player)
print("list_player_And_dice", list_player_And_dice)
lisasd = list_player_And_dice

for i in range(len(list_player_And_dice)):

    for j in range(len(list_order)):
            if(list_player_And_dice[i][0] == list_order[j]):
                list_player_And_dice.remove(list_player_And_dice[i])
                list_player_And_dice.append(new_dice[j])


print("list_player_And_dice", list_player_And_dice)

