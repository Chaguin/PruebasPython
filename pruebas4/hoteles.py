class Hotel(object):

	def __init__(self, nombre = '*', ubicacion = '*',
					puntaje = 0, precio = float("inf")):
		if es_cadena_no_vacia(nombre):
			self.nombre = nombre
		else:
			raise TypeError("El nombre debe ser una cadena no vacia")
			
		if es_cadena_no_vacia(ubicacion):
			self.ubicacion = ubicacion
		else:
			raise TypeError("la ubicacion debe ser una cadena no vacia")
			
		if es_numero(puntaje):
			self.puntaje = puntaje
		else:
			raise TypeError("El puntaje debe ser un numero")
		
		if es_numero(precio):
			if precio !=0:
				self.precio=precio
			else:
				self.precio=float("inf")
		else:
			raise TypeError("El precio debe ser un numero")
			
	def __str__(self):
		return self.nombre + "de" + self.ubicacion +\
			"- puntaje: " +str(self.puntaje)+ "-precio: " + \
			str(self.precio)+ " pesos."
			