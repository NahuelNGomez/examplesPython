#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

mphour = input("Cuánto cobra por hora?")

hours = input("Cuánto trabajó? en horas")

salary = int(mphour) * int(hours)

print("Debe cobrar " + str(salary) + "$")