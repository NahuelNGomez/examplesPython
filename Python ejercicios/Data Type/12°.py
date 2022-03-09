#Una panadería vende barras de pan a 3.49$ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

breadCost = 3.49
sale = 0.6
oldBread = float(input("Barras de pan que no son de hoy: "))
print(
    "Precio total de pan: "+ str(oldBread*breadCost)+" \n"
    "Descuento -> 60%: " + str((oldBread*breadCost)*sale) +" \nTotal a pagar: "+ str((oldBread*breadCost) - (oldBread*breadCost)*sale))