# -*- coding: utf-8 -*-
from Tkinter import *
root = Tk()

li = 'Diego Matias Martin Carla Lorena Roberto'.split()
mov = 'los juegos del hambre Cars La caida del halcon negro'.split()
listb = Listbox(root)
listb2=Listbox(root)
for item in li:
    listb.insert(0, item)

for item in mov:
    listb2.insert(0, item)

listb.pack()
listb2.pack()
root.mainloop()