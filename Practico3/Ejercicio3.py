from datetime import datetime

class Persona(object):
	def __init__(self, rut, nombre, fecha_nac, genero):
		self.rut = rut
		self.nombre = nombre
		self.fecha_nac = fecha_nac
		self.genero = genero

	def obtener_edad(self):
		hoy = datetime.now().date()
		#print "La fecha de hoy es "+str(hoy)
		yearactual = datetime.now().year
		naci=self.fecha_nac[0:4]
		#print naci
		print "La edad es "+str(yearactual-int(naci))
		
		#print yearactual
		monthactual = datetime.now().month
		#print monthactual
		dayactual = datetime.now().day
		#print dayactual


class Nota(object):
 	def __init__(self, valor, ponderacion, ramo, carrera):
 		self.valor = valor
 		self.ponderacion = ponderacion
 		self.ramo = ramo
 		self.carrera = carrera

 	def obtener_valor(self):
		print "El valor es "+str(self.valor)
 	def obtener_ponderacion(self):
		print "La ponderacion es "+str(self.ponderacion)
 	def modificar(self,valor):
		self.valor = valor
		print "El valor modificado es "+str(self.valor)

class Alumno(Persona):
	def __init__(self,correo,carrera,promocion,notas):
		#super(Alumno,self).__init__()
		self.correo = correo
		self.carrera = carrera
		self.promocion = promocion
		self.notas = notas
		
	def agregar_nota(self,notas):
		for i in range(len(notas)):
			self.notas.append(notas[i])
	def PGA(self):
		promedio=0
		for i in range(len(self.notas)):
			promedio = promedio+self.notas[i]
		promedio = promedio/len(self.notas)
		print "El promedio es: "+str(promedio)
	def promedio_por_ramo(self):
		pass
		
if __name__=="__main__":		
	p = Persona("188868354-1","Camilo","1994-08-07","Masculino")
	p.obtener_edad()
	n = Nota(50,30,"Taller de construccion de software","ICI")
	n.obtener_valor()
	n.obtener_ponderacion()
	n.modificar(33)
	a = Alumno("asdasd@alumnos.uach.cl","ICI",2012,[3.0,7.0,5.0,4.5,6.8])
	a.agregar_nota([3.4,6.2,3.6,7.0])
	a.PGA()
	a.promedio_por_ramo()
