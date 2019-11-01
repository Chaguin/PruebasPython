# -*- coding: utf-8 -*-
numero=int(input("Dame un nume con varias cifras"))

if numero<100 and numero>=10:
    print ("El numero es de dos digitos")
elif numero<10:
    print ("el numero es de un digito")
else:
    if numero>=100 and numero<1000:
        print ("el numero es de tres cifras")
