#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

n = int(input("Un numero: "))
m = int(input("Otro numero: "))
c = int(n/m)
rest = round(((n/m)*100-c)/100,3)
print(str(n) + "dividido"+ str(m) + "da un cociente: " + str(c) + " y un resto: "+ str(rest))