class Millas:
	def __init__(self, distancia=0):
		self._distancia = distancia

	def convertir_a_kilometros(self):
		return self._distancia * 1.609344

	# Método getter
	def get_distancia(self):
		return self._distancia

	# Método setter
	def set_distancia(self, valor):
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		self._distancia = valor


if __name__ == '__main__':
	objeto1 = Millas(0)
	objeto1.set_distancia(200)

	print(objeto1.get_distancia())






