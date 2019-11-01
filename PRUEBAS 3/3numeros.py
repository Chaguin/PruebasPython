# -*- coding: utf-8 -*-
uno = int(input("dame un numero"))
dos = int(input("Dame otro numero"))
tres = int(input("dame otro numero"))

if uno>dos and uno>tres:
    mayor=uno
elif dos>uno and dos>tres:
    mayor=dos
else:
    mayor = tres

print ("el mayor es: ",mayor)

