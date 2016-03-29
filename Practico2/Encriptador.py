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
vp.geometry("540x400")
vp.title("Encriptador")
#app.config(bg="grey")
#app.resizable(0,0)
    
etiqueta1 = Label(vp,text= "Ingrese la frase a encriptar: ")
etiqueta1.place(x=30,y=30)  

mitexto = StringVar()
textoentry = StringVar()

entrada_txt = Entry(vp,width=59,bd=5, textvar=textoentry,bg="lightyellow")
entrada_txt.place(x=30,y=60)  

etiqueta2 = Label(vp,text= "Seleccione el metodo de encriptacion: ")
etiqueta2.place(x=30,y=120)

opcion = IntVar()
cenit = Radiobutton(vp,text="Cenit-Polar",value=1,variable=opcion)
cenit.place(x=320,y=120)
cesar = Radiobutton(vp,text="Cesar",value=2,variable=opcion)
cesar.place(x=430,y=120)

etiqueta3 = Label(vp,text= "Especifique el salto para la encriptacion cesar: ")
etiqueta3.place(x=30,y=150)

valor = StringVar()
combo = Spinbox(vp,from_ = 0, to = 50, textvariable = valor)
combo.place(x=330,y=150)

etiqueta4 = Label(vp,text= "Resultado: ")
etiqueta4.place(x=30,y=200)
etiqueta5 = label_resultado = Label(vp,textvar=mitexto,bg = "lightyellow")
etiqueta5.place(x=30,y=230)

boton = Button(vp,text="Encriptar",width=13,height=2,bg="lightgreen", command=lambda: cambiar_stringbar(textoentry.get(),mitexto))
boton.place(x=200,y=325)

########################################################################

def cambiar_stringbar(nuevotexto,stringvar):  #metodo principal al hacer click en el boton
    #stringvar.set(nuevotexto)
    if valor.get() == 0:
		tkMessageBox.showinfo( "Hello Python", "Hello World")
    stringvar.set(obtenerradiobutton(nuevotexto))
    
    
########################################################################

def obtenerspinbox():	#obtenemos el valor correspondiente a cuanto se correra cada caracter de la frase
	print ("El valor del spinbox es: " + valor.get())
	return valor.get()

########################################################################

def obtenerradiobutton(frase):   #metodo que gestiona las formas de encriptacion
	####CENIT-POLAR####
	if opcion.get() == 1:
		print ("Ha seleccionado el metodo: Cenit-Polar")
		print ("Su frase es: "+frase)
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
		
		return cadena
	####CESAR####
	elif opcion.get() == 2:
		print ("Ha seleccionado el metodo: Cesar")
		abc = string.ascii_lowercase
		palabra_encriptada = ""
		buscar = ""
		for (letra) in (frase):
			if letra != " ":
				buscar = (abc.index(letra.lower())+obtenerspinbox()) % len(abc)
				palabra_encriptada += (abc[buscar])
			else:
				palabra_encriptada += (letra)
		
		return palabra_encriptada

########################################################################

vp.mainloop()


#def helloCallBack():
#   tkMessageBox.showinfo( "Hello Python", "Hello World")
