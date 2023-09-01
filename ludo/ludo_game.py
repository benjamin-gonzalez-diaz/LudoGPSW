import random

# Función para lanzar el dado
def lanzar_dado():
    return random.randint(1, 6)

# Clase para representar a un jugador
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = 0  # Inicialmente, todos los jugadores están en la casilla de inicio
    
    def avanzar(self, pasos):
        self.posicion += pasos

# Función para determinar el jugador que comienza
def determinar_primer_jugador(jugadores):
    valores_dados = []
    for jugador in jugadores:
        resultado_dado = lanzar_dado()
        print(f"{jugador.nombre} lanzó un {resultado_dado}")
        valores_dados.append((jugador, resultado_dado))
    
    valores_dados.sort(key=lambda x: x[1], reverse=True)
    print(f"\n{valores_dados[0][0].nombre} comienza el juego con el valor más alto en el dado ({valores_dados[0][1]})\n")
    print(valores_dados)
    primer_jugador = valores_dados[0][0]
    return primer_jugador

# Función principal del juego
def jugar_ludo():
    num_jugadores = int(input("Cantidad de jugadores entre 2-4: "))
    if num_jugadores < 2 or num_jugadores > 4:
        print("El número de jugadores debe estar entre 2 y 4.")
        return
    
    jugadores = []
    for i in range(1, num_jugadores + 1):
        nombre = (f"-> Jugador_{i} ")
        jugadores.append(Jugador(nombre))
    
    primer_jugador = determinar_primer_jugador(jugadores)
    
    # Continuar el juego hasta que un jugador alcance la casilla final
    while True:
        for jugador in jugadores:
            input(f"{jugador.nombre}, presiona Enter para lanzar el dado...")
            resultado_dado = lanzar_dado()
            print(f"{jugador.nombre} lanzó un {resultado_dado}")
            
            jugador.avanzar(resultado_dado)
            
            if jugador.posicion >= 100:
                print(f"{jugador.nombre} ha ganado. ¡Felicidades!")
                return

if __name__ == "__main__":
    jugar_ludo()
