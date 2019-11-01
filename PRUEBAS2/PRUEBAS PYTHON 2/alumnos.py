# -*- coding: utf-8 -*-
class Alumnos:

    def __init__(self):
        self.nombre=[]
        self.calif=[]

    def menu(self):
        cerrar=0
        while cerrar !=4:
            title_menu="ESTE ES EL MENU".capitalize()
            print (title_menu.center(50,"="))
            print ("1. Cargar Alumnos")
            print ("2. Listar Alumnos")
            print ("3. Listado de alumnos con notas altas")
            print ("4. Finalizar programa")
            cerrar=int(input("Tecle su opcion: "))
            print ("*******************************")


            if cerrar==1:
                self.cargar()
            elif cerrar==2:
                self.listar()
            elif cerrar==3:
                self.notas_altas()
            elif cerrar==4:
                break


    def cargar(self):
        for  x in range(5):
            alumno=str(input("Ingresa el nombre del alumno: "))
            self.nombre.append(alumno)
            calificacion=int(input("La nota del alumno: "))
            self.calif.append(calificacion)
            print ("*******************************")

    def listar(self):
        if len(self.nombre)==0:
            print ("La lista esta vacia")
            alumno1.menu()
        for x in range(5):
            print (self.nombre[x],".....",self.calif[x])
            print ("******************************")

    def notas_altas(self):
        if len(self.calif)==0:
            print ("La lista de calificaciones esta vacia")
            print ("*************************************")
            alumno1.menu()
        else:
            self.conta=[]
            for x in range(5):
                if self.calif[x]>7:
                    self.mayor=self.calif[x]
                    self.conta.append
            print ("Las calificaciones mayores a 7 son: ",self.conta)
        alumno1.menu()

alumno1=Alumnos()
alumno1.menu()
