# -*- coding: utf -8 -*-
########################################################################
#AUTOR: CAMILO ALEXANDER ALARCON ROMERO
#UACH - CAMPUS MIRAFLORES - INSTITUTO DE INFORMATICA
#TALLER DE CONSTRUCCION DE SOFTWARE
#VALDIVIA MARZO 2016
########################################################################
from Tkinter import *
import sys
import string 
import tkMessageBox
vp=Tk()
#vp = Frame(app)  #ventana principal
#vp.grid(column=0, row=0,padx=(50,50),pady=(10,10))
#vp.columnconfigure(0,weight=1)
#vp.rowconfigure(0,weight=1)
vp.geometry("540x360")
vp.title("Encriptador")
#app.config(bg="grey")
#app.resizable(0,0)
def info():
	tkMessageBox.showinfo(title="Información",message="AUTOR: CAMILO ALEXANDER ALARCÓN ROMERO\n\nPROFESOR: CRISTIAN RODRIGO ROJAS PÉREZ\n\nRAMO: TALLER DE CONSTRUCCIÓN DE SOFTWARE\n\nUACH - CAMPUS MIRAFLORES - INSTITUTO DE INFORMÁTICA\n\nVALDIVIA MARZO 2016")
	
menu1=Menu(vp)
vp.config(menu=menu1)
informacion=Menu(menu1)
informacion.add_command(label="Obtener Informacion",command = info)
informacion.add_command(label="Salir",command=vp.destroy)
menu1.add_cascade(label="Información",menu=informacion)

etiqueta1 = Label(vp,text= "Ingrese la frase a encriptar: ",font=("Agency FB",12))
etiqueta1.place(x=30,y=30)  

mitexto = StringVar()
textoentry = StringVar()

entrada_txt = Entry(vp,width=59,bd=5, textvar=textoentry,bg="lightyellow")
entrada_txt.place(x=30,y=60)  

etiqueta2 = Label(vp,text= "Seleccione el método de encriptación: ",font=("Agency FB",11))
etiqueta2.place(x=30,y=120)

opcion = IntVar()
cenit = Radiobutton(vp,text="Cenit-Polar",value=1,variable=opcion,command=lambda: estadoradio())
cenit.place(x=325,y=120)
cesar = Radiobutton(vp,text="César",value=2,variable=opcion,command=lambda: estadoradio())
cesar.place(x=430,y=120)

etiqueta3 = Label(vp,text= "Especifique el salto para la encriptación césar: ",font=("Agency FB",11))
etiqueta3.place(x=30,y=150)

valor = StringVar()
combo = Spinbox(vp,from_ = 0, to = 50, textvariable = valor, width=5,bg="lightyellow")
combo.place(x=405,y=150)

etiqueta4 = Label(vp,text= "Resultado: ",font=("Agency FB",12))
etiqueta4.place(x=30,y=200)

etiquetaresultado = Label(vp,textvar=mitexto,bg = "lightblue",font=("Agency FB",10))
etiquetaresultado.place(x=30,y=230)

""""entrada = ""
entrada = textoentry.get()
boton = Button(vp,text="Encriptar",font=("Agency FB",12),width=13,height=2,bg="lightgreen", command=lambda: clickbutton(mitexto))"""

boton = Button(vp,text="Encriptar",font=("Agency FB",12),width=13,height=2,bg="lightgreen", command=lambda: clickbutton(textoentry.get(),mitexto))
boton.place(x=200,y=280)

########################################################################

def modifica(nuevotexto,mitexto):
	#stringvar.set(nuevotexto) .
    mitexto.set(obtenerradiobutton(nuevotexto))
    
########################################################################

def estadoradio():
	if opcion.get() == 1:
		combo.config(state=DISABLED)
	else:
		combo.config(state=NORMAL)

########################################################################

""""def clickbutton(mitexto):  #metodo principal al hacer click en el boton
	#entrada = textoentry.get()
    entrada = entrada_txt.get()
    modifica(entrada,mitexto)
    """
def clickbutton(nuevotexto,mitexto):  #metodo principal al hacer click en el boton
    #stringvar.set(nuevotexto)
    mitexto.set(obtenerradiobutton(nuevotexto))
    
########################################################################

def obtenerspinbox():	#obtenemos el valor correspondiente a cuanto se correra cada caracter de la frase
	print ("El valor del spinbox es: " + valor.get())
	return valor.get()

########################################################################

def obtenerradiobutton(frase):   #metodo que gestiona las formas de encriptacion
	palabra_encriptada=""
	
	####CENIT-POLAR####
	if opcion.get() == 1:
		listacenit = ['c','e','n','i','t'] 
		listapolar = ['p','o','l','a','r']
		cenitt = "cenit"
		polarr = "polar"
		print
		print ("Ha seleccionado el método: Cenit-Polar")
		print ("Su frase es: "+frase)
		fr = []
		frase = str(frase.lower())
		indice=""
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
			for c in cenitt:
				if f == c:
					indice = cenitt.index(str(c))
					frasecenit = frasecenit.replace(f,polarr[indice])
		frase_encrypt = frasepolar
		for f in frasepolar:
			for p in polarr:
				if f == p:
					indice = polarr.index(str(p))
					frasepolar = frasepolar.replace(f,cenitt[indice])
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
		for i in range(len(fr)):
			palabra_encriptada = palabra_encriptada + fr[i]
		print "La cadena encriptada en Cenit-Polar es: " + palabra_encriptada 
		
		
	####CESAR####
	
	elif opcion.get() == 2:
		print
		print ("Ha seleccionado el metodo: César")
		print ("Su frase es: "+frase)
		numero = ["0","1","2","3","4","5","6","7","8","9",""]
		frase = frase.lower()
		abc = string.ascii_lowercase
		for letra in frase:
			cont=0
			for char in abc:
				if letra == char:
					if int(valor.get())+cont >= len(abc) or (letra in numero):
						palabra_encriptada = palabra_encriptada+abc[(int(valor.get())+cont)-(len(abc))]
					else:
						palabra_encriptada = palabra_encriptada+abc[(int(valor.get())+cont)]
				else:
					cont += 1
		print "La cadena encriptada en César es: " + palabra_encriptada
		
	return palabra_encriptada

########################################################################

vp.mainloop()
