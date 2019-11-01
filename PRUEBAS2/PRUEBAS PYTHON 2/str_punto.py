# -*- coding: utf-8 -*-
class punto:

    def __init__(self, x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"

punto1=punto(10, 3)
punto2=punto(3, 4)
print (punto1)
print (punto2)
