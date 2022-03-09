#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.


mass = float(input("introduce su peso: "))
height = float(input("Introduzca su altura: "))

imc = mass/(height**2)

imc = round(imc,2)

print("Tu índice de masa corporal es " + str(imc))