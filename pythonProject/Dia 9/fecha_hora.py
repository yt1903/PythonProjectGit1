"""
MÒDULO Para manejo de fecha hora datetime
"""

# import datetime
from datetime import datetime,date

"""mi_hora = datetime.time(17,40)
print(mi_hora)
print(mi_hora.hour)
print(mi_hora.minute)
print(type(mi_hora))"""

"""mi_fecha = datetime.date(2025,12,1)
print(mi_fecha)
print(mi_fecha.today())
print(mi_fecha.ctime())
print(mi_fecha.year)
print(mi_fecha.month)
print(mi_fecha.day)"""

mi_fecha= datetime(2025,12,31,12,50)
mi_fecha= mi_fecha.replace(month=3)
print(mi_fecha)
print(mi_fecha.minute)

nacimieto = date(1996,5,12)
defuncion = date(2090,3,12)
vida = defuncion - nacimieto
print(vida)
