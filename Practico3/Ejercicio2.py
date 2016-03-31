class Vehiculo(object):
	def _init_(self, kilometraje,bencina,rendimiento,encendido):
		self.kilometraje = kilometraje
		self.bencina = bencina
		self.rendimiento = rendimiento
		self.encendido = encendido
	def Encender(self):
		print "Se ha encendido el auto"
		self.encendido = True
	def Apagar(self):
		print "Se ha apagado el auto"
		self.encendido = False
	def Mover(self,km):
		#x = km/self.rendimiento
		self.encendido == True
		if self.bencina > km/self.rendimiento:
				print "Se ha movido el auto"
				self.bencina = self.bencina - km/self.rendimiento
		else:
			print "El auto no tiene bencina, por lo cual no se puede mover"
			self.encendido = False
	def getKilometraje(self):
		print "El kilometraje del auto es " + str(self.kilometraje)
	def getBencina(self):
		print "La bencina disponible es " + str(self.bencina) 
	def setBencina(self,b):
		self.encendido = False
		self.bencina = self.bencina + b
		print "Ha cargado bencina en el auto"
		print "Su bencina es "+str(self.bencina)
		
class Acoplado(object): 
	def __init__(self,Ruedas,Peso,carga):
		self.Ruedas = int(Ruedas)
		self.Peso = float(Peso)
		self.carga = str(carga)

class Camion(Vehiculo): 
	def __init__(self,Peso,Ruedas):
		super(Camion,self).__init__()	 
		self.Peso = float(Peso)
		self.Ruedas = int(Ruedas)
		self.Acoplados = []
		
	def agregar_acoplados(self,Ruedas,Peso,carga):
		new = Acoplado(Ruedas,Peso,carga)
		self.Acoplados.append(new)
	def quitar_acoplados(self):
		if len(self.Acoplados)>0:
			self.Acoplados.pop(len(self.Acoplados)-1)
	def obtener_acoplados(self):
		print "Los acoplados son "+str(self.Acoplados)
	def obtener_ruedas(self):
		print "Las ruedas son "+str(self.Ruedas)
	def obtener_peso(self):
		print "El peso es "+str(self.Peso)+" kg"
		
if __name__=="__main__":
	
	ob=Camion(100,4)
	
	ob.agregar_acoplados(4,1000,"Maiz")
	ob.obtener_acoplados()
	ob.obtener_ruedas()
	ob.obtener_peso()
