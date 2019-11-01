# -*- coding: utf-8 -*-
#importamos la libreria xlwt y datetime
import xlwt
from datetime import datetime

#creamos un estilo de la fuente
style0 = xlwt.easyxf('font: name Times New Roman, color red, bold on')
#creamos un estilo de una fecha
style1 = xlwt.easyxf('',num_format_str= 'DD-MMM-YY')
#leemos el archivo
wb = xlwt.Workbook()
#agregamos un nombre a la hoja A test sheet y le decimos que
#podemos escribir en las celdas con cell
ws = wb.add_sheet('A Test Sheet', cell_overwrite_ok=True)
#en la columna y fila 0,0 se escribe Test con el estilo0
ws.write(0, 0, 'Test', style0)
#en la columna y fila 1,0 ponemos la fecha
ws.write(1, 0, datetime.now(), style1)
#en la columna y fila 2,0 escribimos un 4
ws.write(2, 0, 4)
#en la columna y fila 2,1 escribimos un 1
ws.write(2, 1, 1)
#en la columna y fila 2,2 ponemos una formula que suma la posiciones A3+B3
ws.write(2, 2, xlwt.Formula("A3+B3"))
#guardamos el archivo
wb.save('prueba.xls')