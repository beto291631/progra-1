import operator
import os

def sumar(a, b):
    return operator.add(a, b)

def restar(a, b):
    return operator.sub(a, b)

def multiplicar(a, b):
    return operator.mul(a, b)

def dividir(a, b):
    if b != 0:
        return operator.truediv(a, b)
    else:
        return "Error: No se puede dividir entre cero."

def calcular(operador, num1, num2):
    operadores = {
        '+': sumar,
        '-': restar,
        '*': multiplicar,
        '/': dividir
    }

    if operador in operadores:
        return operadores[operador](num1, num2)
    else:
        return "Operador inválido."

def limpiar_pantalla():
    if os.name == 'nt':  # Para sistemas Windows
        os.system('cls')
    else:  # Para sistemas basados en Unix/Linux
        os.system('clear')

def main():
    historial = []

    while True:
        print("Calculadora básica")
        print("Operaciones disponibles: +, -, *, /")
        print("Para limpiar la pantalla, presione 'L'. Para salir, presione 'Q'.")

        expresion = input("Ingrese la expresión (o 'L' para limpiar, 'Q' para salir): ")

        if expresion == 'L':
            limpiar_pantalla()
            continue
        elif expresion == 'Q':
            break

        try:
            num1, operador, num2 = expresion.split()
            num1 = float(num1)
            num2 = float(num2)
            resultado = calcular(operador, num1, num2)
            historial.append(f"{expresion} = {resultado}")
            print("El resultado es:", resultado)
        except ValueError:
            print("Expresión inválida. Asegúrese de ingresar un número, un operador y otro número.")

    print("Historial de cálculos:")
    for item in historial:
        print(item)

main()

