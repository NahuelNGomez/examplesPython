#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

date = input("introduzca su fecha de nacimiento en formato dd/mm/aaaa: ")
day = date[:date.find("/")]
date = date[date.find("/")+1:len(date)]
month = date[:date.find("/")]
year = date[date.find("/")+1:]
print("día: " + day +"\nmés: "+ month + "\naño: " + year)