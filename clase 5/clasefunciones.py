# a veces necesitamos repetir ciertos fracmentos de codigo y en lugar de escribir nuevamente lo mismo una y otra vez, en programacion existe loque se conoce como funciones, las mismas las usamos para realizar tareas que se repiten 

def saludo():
    print("hola clase, buenas")
    print("Mi nombre es Alberto")

saludo()

# En ocaciones las funciones necesitan imformacion especifica para realazar las tareas para las cuales fueron programadas, a estos elementyos se le conoce como parametro.

def saludo2(nombre, apellido):
    print("hola espero que estes bien", nombre)
    print("nombre:", nombre)
    print("apellido:", apellido)

nombre = "Nayarith"
apellido = "Quesada"
saludo2(nombre, apellido)

# retorno
# una funcion puede devolver un valor al codigo que la llamo.
# las funciones se escriben para realizar tareas, y  aveces es posible que necesitamos el resultado de las tareas, eso se puede hacer por medio de un RETURN

def edad(edad):
    label = "La edad del usuario es: " + edad
    return label

print(edad("34"))

def impar(num):
    if num % 2 == 0 :
        label =str (num) + "espar"
    else:
        label = str(num)+ "es inpar"
    
    return label
print(impar(25))
print(impar(15))
print(impar(20))

