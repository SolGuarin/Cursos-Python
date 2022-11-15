class Millas:
	def __init__(self, distancia=0):
		self.distancia = distancia

	def convertir_a_kilometros(self):
	    return (self.distancia * 1.609344)


# Creamos un nuevo objeto
avion = Millas()

# Indicamos la distancia
avion.distancia = 200

# Obtenemos el atributo distancia
print(avion.distancia)
print(avion.convertir_a_kilometros())
