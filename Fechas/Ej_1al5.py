import datetime

"""
Crea una función que obtenga la fecha y hora actuales, luego formatea la fecha para que
se muestre en el formato DD/MM/YYYY HH:MM:SS.
 Usa datetime.now() para obtener la fecha y hora actual.
 Formatea la fecha en el formato DD/MM/YYYY HH:MM:SS usando strftime"""
def Fecha():
    fecha = datetime.now()
    fecha_formateada = fecha.strftime("%d/%m/%Y %H:%M:%S")
    
    return fecha_formateada
print(Fecha())