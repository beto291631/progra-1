import random

def jugar():
    jugador1 = 0
    jugador2 = 0
    deuce = False
    ventaja = False

    while True:
        print("Marcador: {}-{}".format(jugador1, jugador2))

        if deuce:
            if ventaja:
                print("Ventaja jugador 1: V / Ventaja jugador 2: ")
            else:
                print("Ventaja jugador 1:  / Ventaja jugador 2: V")
        else:
            print("Marcador: {}-{}".format(puntajes[jugador1], puntajes[jugador2]))

        jugador_ganador = input("¿A qué jugador se le asigna el punto? (1 o 2): ")

        if jugador_ganador == '1':
            if deuce and ventaja:
                jugador1 += 1
                print("¡Jugador 1 gana el juego!")
                break
            elif jugador1 == 40 and jugador2 == 40:
                deuce = True
                ventaja = True
            elif jugador1 == 40 and jugador2 < 40:
                print("¡Jugador 1 gana el juego!")
                break
            elif jugador1 < 40:
                jugador1 += 1
        elif jugador_ganador == '2':
            if deuce and ventaja:
                jugador2 += 1
                print("¡Jugador 2 gana el juego!")
                break
            elif jugador1 == 40 and jugador2 == 40:
                deuce = True
                ventaja = True
            elif jugador2 == 40 and jugador1 < 40:
                print("¡Jugador 2 gana el juego!")
                break
            elif jugador2 < 40:
                jugador2 += 1
        else:
            print("Opción inválida. Intenta nuevamente.")

        if jugador1 > 40 or jugador2 > 40:
            print("¡Juego terminado!")
            break

# Diccionario para mapear los puntajes a sus representaciones en el tenis
puntajes = {
    0: '0',
    15: '15',
    30: '30',
    40: '40'
}

while True:
    print("Bienvenido al juego de tenis!")
    opcion = input("Selecciona una opción (1: Jugar manualmente, 2: Jugar automáticamente): ")

    if opcion == '1':
        jugar()
    elif opcion == '2':
        jugador_ganador = random.choice(['1', '2'])
        print("El punto se le asigna al Jugador {}".format(jugador_ganador))
        jugar()
    else:
        print("Opción inválida. Intenta nuevamente.")
