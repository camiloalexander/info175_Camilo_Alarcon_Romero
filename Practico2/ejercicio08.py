# -*- coding: utf -8 -*-
import string

def encrypt(word, jump):
    abc = string.ascii_lowercase
    palabra_encriptada = ""
    for letra in word:
        if letra != " ":
            buscar = (abc.index(letra.lower())+jump) % len(abc)
            palabra_encriptada += (abc[buscar])
        else:
            palabra_encriptada += (letra)
    
    return palabra_encriptada


if __name__ == "__main__":
	x = raw_input("Ingrese frase a encriptar: ")
	while x.isalpha() == False:
		x = raw_input("Ingrese frase a encriptar: ")
		
	y = raw_input("Ingrese cantidad a mover: ")
	while y.isdigit() == False:
		y = raw_input("Ingrese cantidad a mover: ")
	
	str(x)
	int(y)
	
	print(encrypt(x, y))
    
