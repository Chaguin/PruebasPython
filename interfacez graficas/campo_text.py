import sys.arg

from tkinter import *

def hacer_click():
    try:
        _valor = int (entrada_texto.get())
        _valor = _valor * 5
        etiqueta.config(text=_valor)
    except ValueError:
        etiqueta.config(text="Introduce un numero!")

app = tk()
app.title("Mi segundo mensaje a Anita")

vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady(10,1))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta.label(vp, text="Valor")
etiqueta.grid(column=2, row=2, sticky=(W,E))

boton = Button(vp, text="Ok", comand=hacer_click)
boton.grid(column=1, row=1)

valor = ""
entrada_texto = Entry(vp, width=10, textvariable=valor)
estrada_texto.grid(column=2, row=1)

app.mainloop()