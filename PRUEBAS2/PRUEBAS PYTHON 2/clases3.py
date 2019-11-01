# -*- coding: utf-8 -*-
class Operacion:

    def __init__(self):
        self.valor1=int(input("Ingrese el primer valor: "))
        self.valor2=int(input("Ingrese el segundo valor: "))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        suma=self.valor1+self.valor2
        print ("La suma es: " ,suma)

    def restar(self):
        resta=self.valor1-self.valor2
        print ("La resta es: ",resta)

    def multiplicar(self):
        multiplicar=self.valor1*self.valor2
        print ("La suma es: ",multiplicar)

    def dividir(self):
        dividir=self.valor1/self.valor2
        print ("La division es: ",dividir)

operacion1=Operacion()