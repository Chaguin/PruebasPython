# -*- coding: utf-8 -*-
class Empleado:

    def __init__(self):
        self.nombre=input("Nombre del empeado: ")
        self.sueldo=float(input("Sueldo del empleado: "))

    def imprimir(self):
        print ("NOMBRE: ",self.nombre)
        print ("SUELDO: ",self.sueldo)

    def impuestos(self):
        if self.sueldo>3000:
            print ("Este empleado debe pagar impuestos!")
            print ("*****************************************")
        else:
            print ("No paga no impuestos!")
            print ("*****************************************")

empleado1=Empleado()
empleado1.imprimir()
empleado1.impuestos()
