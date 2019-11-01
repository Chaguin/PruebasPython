# -*- coding: utf-8 -*-
class Alumno:

    def inicializar(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print ("el nombre es:",self.nombre)
        print ("la nota es: ",self.nota)

    def mostrar_estado(self):
        if self.nota>4:
            print ("Es regular")
            print ("******************************")
        else:
            print ("Es irregular")
            print ("******************************")

#programa principal

alumno1=Alumno()
alumno1.inicializar("diego",10)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2=Alumno()
alumno2.inicializar("ana",9)
alumno2.imprimir()
alumno2.mostrar_estado()

alumno3=Alumno()
alumno3.inicializar("luis",3)
alumno3.imprimir()
alumno3.mostrar_estado()