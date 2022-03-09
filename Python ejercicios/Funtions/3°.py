'''
Escribir una función que reciba un número
entero positivo y devuelva su factorial.
'''

def factorial(number):
    sum = 1
    for i in range(1,number+1):
        sum = sum*i
    return sum
number = int(input("Introduzca un numero entero positivo: "))

print("Su factorial es: " +str(factorial(number)))

