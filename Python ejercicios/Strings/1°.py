#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

name = input("Introduzca su nombre: ")

number = int(input("Cuántas veces quiere que aparezca? "))

for i in range(number):
    print(name)