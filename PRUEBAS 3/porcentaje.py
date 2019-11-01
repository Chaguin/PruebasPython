# -*- coding: utf-8 -*-
calif=int(input("Cual es el porcentaje que saco el empleado: "))
if calif>=90:
    print ("Obtuvo el nivel maximo_ ")
elif calif>=75 and calif<90:
    print ("obtuvo el nivel medio_ ")
elif calif>=50 and calif<75:
    print ("obtuvo el nivel regular_ ")
elif calif<50:
    print ("Esta fuera de nivel")
