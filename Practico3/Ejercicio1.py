
class Auto(object):
	def __init__(self, kilometraje,bencina,rendimiento,encendido):
		self.kilometraje = int(kilometraje)
		self.bencina = int(bencina)
		self.rendimiento = int(rendimiento)
		self.encendido = bool(encendido)
	###################
	def Encender(self):
		print "Se ha encendido el auto"
		self.encendido = True
	###################
	def Apagar(self):
		print "Se ha apagado el auto"
		self.encendido = False
	###################
	def Mover(self,kilometraje):
		self.encendido == True
		if self.bencina > kilometraje/self.rendimiento:
				print "Se ha movido el auto"
				self.bencina = self.bencina - kilometraje/self.rendimiento
		else:
			print "El auto no tiene bencina, por lo cual no se puede mover"
			self.encendido = False
	###################
	def getKilometraje(self):
		print "El kilometraje del auto es " + str(self.kilometraje)
	###################
	def getBencina(self):
		print "La bencina disponible es " + str(self.bencina) 
	###################
	def setBencina(self,b):
		self.encendido = False
		self.bencina = self.bencina + b
		print "Ha cargado bencina en el auto"
		print "Su bencina es "+str(self.bencina)
			
if __name__=="__main__":
	
	obj = Auto(13,20,10,True)
	obj.Encender()
	obj.Apagar()
	obj.Mover(34)
	obj.getKilometraje()
	obj.getBencina()
	obj.setBencina(10)
