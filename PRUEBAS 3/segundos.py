# -*- coding: utf-8 -*-

#definir funcion para calculo
def print_asegundos(horas, minutos, segundos):
    segsal = 3600 * horas + 60 * minutos + segundos
    print ("***son ", segsal," segundos***")
    print ("***************************")

#definir funcion para pedir los numeros
def main():
    for x in range (3):
        hs = int(input("Cuantas horas?: "))
        mins = int(input("Cuantos minutos?: "))
        seg = int(input("Cuantos segundos?: "))
        print ("***************************")
        print_asegundos(hs, mins, seg)

main()

