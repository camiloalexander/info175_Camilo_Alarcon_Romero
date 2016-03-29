# -*- coding: utf -8 -*-
import string

listacenit = ['c','e','n','i','t'] 
listapolar = ['p','o','l','a','r']


def encrypt_cenit_polar(frase):
	fr = []
	fras = frase  #copia de frase (por si la necesito)
	fras = str(frase.lower())
	for indice in range(len(fras)):
		letra = fras[indice]
		fr.append(letra)
		copiafr=fr   #copia de la fr (por si la necesito)
		if fr[indice] == "p":
			fr[indice] = fr[indice].replace("p","c")
		if fr[indice] == "o":
			fr[indice] = fr[indice].replace("o","e")
		if fr[indice] == "l":
			fr[indice] = fr[indice].replace("l","n")
		if fr[indice] == "a":
			fr[indice] = fr[indice].replace("a","i")	
		if fr[indice] == "r":
			fr[indice] = fr[indice].replace("r","t")

		if fr[indice] == "c":
			fr[indice] = fr[indice].replace("c","p")
		if fr[indice] == "e":
			fr[indice] = fr[indice].replace("e","o")
		if fr[indice] == "n":
			fr[indice] = fr[indice].replace("n","l")		
		if fr[indice] == "i":
			fr[indice] = fr[indice].replace("i","a")				
		if fr[indice] == "t":
			fr[indice] = fr[indice].replace("t","r")
			
		#fr[indice] = fr[indice].replace("c","p")	
		#fr[indice] = fr[indice].replace("e","o")
		#fr[indice] = fr[indice].replace("n","l")
		#fr[indice] = fr[indice].replace("i","a")
		#fr[indice] = fr[indice].replace("t","r")
		
		#fr[indice] = fr[indice].replace("p","c")
		#fr[indice] = fr[indice].replace("o","e")
		#fr[indice] = fr[indice].replace("l","n")
		#fr[indice] = fr[indice].replace("a","i")
		#fr[indice] = fr[indice].replace("r","t")
		
	print fr
	
	cadena = ""
	for i in range(len(fr)):
		cadena = cadena + fr[i]
	print "La cadena encriptada en Cenit-Polar es: " + cadena 
	
if __name__ == "__main__":
	frase = raw_input("Ingrese frase a encriptar: ")
	print(encrypt_cenit_polar(str(frase)))
