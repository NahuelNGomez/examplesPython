#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

amount = int(input("Cantidad a invertir: "))
interest = float(input("Interés anual (en porcentaje, ej: 25): "))
numberOfYears = int(input("Número de años: "))

capital = round(amount*(interest/100+1)**numberOfYears,3)
print("El capital obtenido de la inversión es: " + str(capital))
