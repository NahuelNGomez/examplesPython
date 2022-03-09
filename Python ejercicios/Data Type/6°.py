#Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos puede ser calculada de la siguiente forma: N(N+1)/2

number = input("introduzca un numero: ")
number = int(number)
sum = number*(number+1)/2

print("La suma de todos los numeros de 1 hasta "+ str(number) + " es "+ str(sum))