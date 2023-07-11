import os

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división entre cero"

def calcular(operador, a, b):
    if operador == "+":
        return sumar(a, b)
    elif operador == "-":
        return restar(a, b)
    elif operador == "*":
        return multiplicar(a, b)
    elif operador == "/":
        return dividir(a, b)
    else:
        return "Error: operador no válido"

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        a = float(input("Ingrese el primer número: "))
        operador = input("Ingrese el operador (+, -, *, /): ")
        b = float(input("Ingrese el segundo número: "))

        resultado = calcular(operador, a, b)
        print("Resultado:", resultado)

        tecla = input("Presione L para limpiar la pantalla o Q para salir: ")
        if tecla == "L" or tecla == "l":
            continue
        elif tecla == "Q" or tecla == "q":
            break

main()


