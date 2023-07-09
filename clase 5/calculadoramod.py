import os

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: No se puede dividir entre cero"

def limpiar_pantalla():
    if os.name == 'nt':  # Verifica si el sistema operativo es Windows
        os.system('cls')  # Borra la pantalla en Windows
    else:
        os.system('clear')  # Borra la pantalla en sistemas Unix-like

def calcular():
    while True:
        limpiar_pantalla()
        print("Calculadora Básica")
        print("Ingrese la operación en el siguiente formato: número1 operador número2")
        print("Operadores disponibles: +, -, *, /")
        print("Presione 'L' para limpiar la pantalla")
        print("Presione 'Q' para salir")

        entrada = input("Operación: ")

        if entrada.upper() == 'Q':  # Salir del programa si se ingresa 'Q'
            break

        if entrada.upper() == 'L':  # Limpiar la pantalla si se ingresa 'L'
            limpiar_pantalla()
            continue

        valores = entrada.split()
        if len(valores) != 3:  # Verificar que se ingresaron 3 valores
            print("Entrada inválida")
            input("Presione Enter para continuar...")
            continue

        try:
            num1 = float(valores[0])
            operador = valores[1]
            num2 = float(valores[2])

            if operador == "+":
                resultado = suma(num1, num2)
            elif operador == "-":
                resultado = resta(num1, num2)
            elif operador == "*":
                resultado = multiplicacion(num1, num2)
            elif operador == "/":
                resultado = division(num1, num2)
            else:
                print("Operación no válida")
                input("Presione Enter para continuar...")
                continue

            print("Resultado:", resultado)
            input("Presione Enter para continuar...")
            
        except ValueError:
            print("Entrada inválida")
            input("Presione Enter para continuar...")

calcular()
