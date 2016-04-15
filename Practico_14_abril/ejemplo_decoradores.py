# -*- coding: utf-8 -*-

LOGIN = True

def autenticado(f):
	def inner(*args, **kwargs):
		if LOGIN:
			f(*args,**kwargs)
		else:
			raise Exception
	return inner
	
def avisar(f):
	#Funcion decorada
	def inner(*args, **kwargs): #(cualquier numero de parametros , metodo(numero = 5) es decir le paso el nombre de la variable y el valor)
		f(*args,**kwargs)
		print "se ha ejecutado %s" % f, __name__
	return inner


#antes de abrir_puerta() me la va a decorar con avisar
@autenticado    #si no tiene permiso no pasa
@avisar
def abrir_puerta():
	print "Abrir puerta"

@autenticado
@avisar
def cerrar_puerta():
	print "Cerrar puerta"
