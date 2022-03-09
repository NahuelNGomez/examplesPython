'''
Los teléfonos de una empresa tienen el siguiente formato 
prefijo-número-extension donde el prefijo es el código del país +54,
y la extensión tiene dos dígitos (por ejemplo +54-913724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato y 
muestre por pantalla el número de teléfono sin el prefijo y la extensión.
'''

number = input("Número de telefono completo?")

print("su numero es: " + number[4:-3])