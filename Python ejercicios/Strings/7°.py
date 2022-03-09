'''
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre
por pantalla otro correo electrónico con el mismo nombre
(la parte delante de la arroba @) pero con dominio .edu.ar.
'''

email = input("Escriba su email: ")

print(email[:email.find('@')] + "@edu.ar")
