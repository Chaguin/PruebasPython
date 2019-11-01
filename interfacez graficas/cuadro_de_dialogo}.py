# -*- coding: utf-8 -*-
from tkinter import *

app = Tk()
app.title("Saludando a Anita")
etiqueta = Label(app, text = "Hola Anita")
boton = Button(app, text = "Adios")

etiqueta.pack()
boton.pack()
app.mainloop()