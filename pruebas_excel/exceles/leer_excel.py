# -*- coding: utf-8 -*-
import xlrd
book = xlrd.open_workbook('reporte.xlsx','rb')
print ("el numero de worksheets es: ",book.nsheets)
print ("el nombre de worsheet es: ",book.sheet_names())
sh = book.sheet_by_index(0)
print (sh.name, sh.nrows, sh.ncols)
print ("Contenido de (2,0) es: ", sh.cell(rowx= 2, colx=1).value)
for rx in range(sh.nrows):
    if rx ==True:
        print (sh.row(rx))