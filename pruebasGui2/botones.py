# -*- coding: utf-8 -*-
from Tkinter import *

def decir_hola():
    print ("Estoy diciendo =Hola=")

ventana = Tk()
boton = Button(ventana, text='Que estas diciendo? ',command=decir_hola)
boton.pack()

ventana.mainloop()