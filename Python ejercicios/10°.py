#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

dollWeight = 75
clownWeight = 112

dollsSold = int(input("¿Cuántas muñecas se vendieron hoy? "))

clownsSold = int(input("¿Cuántos payasos se vendieron hoy? "))

totalWeight = str(round((dollWeight*dollsSold + clownWeight*clownsSold)/1000, 2))

print("El peso total del paquete que será enviado es de: " + totalWeight + " kilos")
