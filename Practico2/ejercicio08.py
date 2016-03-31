# -*- coding: utf -8 -*-
import string
numero = ["0","1","2","3","4","5","6","7","8","9",""]

def encrypt(word, jump):
	jump = int(jump)
	word = word.lower()
	abc = string.ascii_lowercase
	palabra_encriptada = ""
	for letra in word:
		cont=0
		for char in abc:
			if (letra == char or (letra in numero)):
				if jump+cont >= len(abc):
					palabra_encriptada = palabra_encriptada+abc[cont + jump -len(abc)]
				else:
					palabra_encriptada = palabra_encriptada+abc[(cont + jump)]
			else:
				cont += 1
	return palabra_encriptada


if __name__ == "__main__":
	word = raw_input("Ingrese frase a encriptar: ")
	jump = raw_input("Ingrese cantidad a mover: ")
	while jump.isdigit() == False:
		jump = raw_input("Ingrese cantidad a mover: ")
	int(jump)
	print(encrypt(word, jump))
