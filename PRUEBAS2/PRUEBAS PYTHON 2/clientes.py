# -*- coding: utf-8 -*-
class Clientes:

    suspendido=[]

    def __init__(self, codigo, nombre):
        self.codigo=codigo
        self.nombre=nombre

    def imprimir(self):
            print ("Codigo: ",self.codigo)
            print ("Nombre: ",self.nombre)
            self.esta_suspendido()

    def esta_suspendido(self):
        if self.codigo in Clientes.suspendido:
            print ("El cliente esta suspendido")
        else:
            print ("No esta suspendido")
        print ("***********************************")

    def suspender(self):
        Clientes.suspendido.append(self.codigo)

cliente1=Clientes(1, "A")
cliente2=Clientes(2, "B")
cliente3=Clientes(3, "C")
cliente4=Clientes(1, "D")

cliente3.suspender()
cliente4.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print (Clientes.suspendido)

