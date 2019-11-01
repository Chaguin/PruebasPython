# -*- coding: utf-8 -*-
class Panaderia():

    def __init__(self, panes, masa):
        self.panes = panes
        self.masa = masa
        print ("En la tienda hay ",self.panes," y ",self.masa,"kilos de masa pero no la vendo")

    def vender(self):
        if self.panes > 0:
            self.panes -= 1
            print ("Se vendio un pan:::::")
        else:
            print ("Lo sentimos no hay mas pan para vender")

    def cocer(self, piezas):
        self.panes += piezas
        print ("Se cocio un pan mas")

#panaderia1 = Panaderia(3,4)
panaderia2 = Panaderia(1,2)

panaderia2.vender()
panaderia2.vender()

panaderia2.cocer(1)
panaderia2.vender()