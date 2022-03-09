'''
Escribir una función que convierta un número en decimal.
 
'''
def changeToDecimal(number, format):
    sum = 0

    for i in range(len(number)):
        n = 0
        n = int(((int(number)%(10**(i+1)))-n)/(10**(i)))
        sum = sum+ (format**i*n)
    return sum


number = input("escribe un numero: ")
format = int(input("escriba el formato en el que se encuentra: "))
print("El numero en decimal es: " +str(changeToDecimal(number,format)))
