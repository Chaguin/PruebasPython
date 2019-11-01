# -*- coding: utf-8 -*-
class Persona:

    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))

    def imprimir(self):
        print ("Nombre: ",self.nombre)
        print ("Edad: ",self.edad)

class Empleado(Persona):

    def __init__(self):
        super(Empleado, self).__init__()
        self.sueldo=float(input("Ingresa el sueldo: "))

    def imprimir(self):
        super().imprimir()
        print("Sueldo: ",self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("El empleado paga impuestos.")
        else:
            print("El empleado no paga impuestos")

empleado1=Persona()
empleado1.imprimir()
print ("*************************")
empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
