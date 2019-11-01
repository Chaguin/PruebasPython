# -*- coding: utf-8 -*-
class Familia:

    def __init__(self, padre, madre, hijos=[]):
        self.padre=padre
        self.madre=madre
        self.hijos=hijos

    def __str__ (self):
        cadena = self.padre+", "+self.madre
        for hi in self.hijos:
            cadena=cadena+", "+hi
        return cadena

familia1=Familia("Cha", "Ibeth",["Naty","Samy"])
familia2=Familia("Cha", "Anita", ["Liz"])
familia3=Familia("Cha", "bb")

print (familia1)
print (familia2)
print (familia3)