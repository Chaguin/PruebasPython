
#Las fechas
from datetime import date
hoy = date.today()
print(hoy)

#localizacion de fecha
import locale
locale.setlocale(locale.LC_ALL, locale.getdefaultlocale())
hoy.strftime("%m-%d-%y- %d%b%Y es %A. hoy es %d de %B.")
