# -*- coding: utf -8 -*-
import string

listacenit = ['c','e','n','i','t'] 
listapolar = ['p','o','l','a','r']
cenit = "cenit"
polar = "polar"

def encrypt_cenit_polar(frase):
	fr = []
	frase = str(frase.lower())
	""""
	for indice in range(len(frase)):
		letra = frase[indice]
		fr.append(letra)
		copiafr=fr   #copia de la fr (por si la necesito)
	"""
	#frase: contiene la frase original 
	#frasecenit: frase modificada solo con las letras de cenit
	#frasepolar: la frase es modificada con las letras de polar
	#frase_encrypt: contiene la union de los cambios en ambas frases (cenit-polar)
	frasecenit = frase
	frasepolar = frase
	frase_encrypt = frase
	for f in frase:
		for c in cenit:
			if f == c:
				indice = cenit.index(c,0)
				frasecenit = frasecenit.replace(f,polar[indice])
	frase_encrypt = frasepolar
	for f in frasepolar:
		for p in polar:
			if f == p:
				indice = polar.index(p,0)
				frasepolar = frasepolar.replace(f,cenit[indice])
	for x in range(len(frase_encrypt)):
		if frase_encrypt[x] != frasepolar[x]:
			fr.append(frasepolar[x])
		if frase_encrypt[x] != frasecenit[x]:
			fr.append(frasecenit[x])
		if frase_encrypt[x] == frasepolar[x] and frase_encrypt[x] == frasecenit[x]:
			fr.append(frasecenit[x])
	#print fr
	#for item in fr:
	#	print item
	cadena = ""
	for i in range(len(fr)):
		cadena = cadena + fr[i]
	print "La cadena encriptada en Cenit-Polar es: " + cadena 
	
if __name__ == "__main__":
	frase = raw_input("Ingrese frase a encriptar: ")
	print(encrypt_cenit_polar(str(frase)))
