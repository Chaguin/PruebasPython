# -*- coding: utf-8 -*-
class persona:

    def __init__(self, per, ape):
        self.persona=per
        self.apellido=ape

    def __str__(self):
        cadena=self.persona+" , "+self.apellido
        return cadena

persona1=persona("cha", "perez")
print(persona1)