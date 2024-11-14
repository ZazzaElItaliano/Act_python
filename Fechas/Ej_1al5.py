from datetime import  datetime,timedelta

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

"""Escribe una función que reciba una cadena en formato DD/MM/YYYY y la convierta en un
objeto datetime usando strptime().
 La cadena debe ser convertida a un objeto datetime.
 Muestra la fecha convertida"""

def convertir_a_fecha(cadena_fecha):
    fecha_objeto = datetime.strptime(cadena_fecha, "%d/%m/%Y")
    return fecha_objeto


cadena_fecha = "15/11/2024"
fecha_convertida = convertir_a_fecha(cadena_fecha)
print("Fecha convertida:", fecha_convertida)

"""Calcular la diferencia en días entre dos fechas
Crea una función que reciba dos cadenas de fecha en formato DD/MM/YYYY y calcule
cuántos días hay entre ambas.
 Convierte ambas cadenas a objetos datetime.
 Resta las dos fechas y devuelve el número de días de diferencia"""
def diferencia_en_dias(fecha1, fecha2):

    fecha_objeto1 = datetime.strptime(fecha1, "%d/%m/%Y")
    fecha_objeto2 = datetime.strptime(fecha2, "%d/%m/%Y")
    

    diferencia = fecha_objeto2 - fecha_objeto1
    return abs(diferencia.days)

fecha1 = "01/01/2024"
fecha2 = "15/11/2024"
dias_de_diferencia = diferencia_en_dias(fecha1, fecha2)
print("Días de diferencia:", dias_de_diferencia)

"""Sumar días a una fecha
Escribe una función que reciba una fecha en formato DD/MM/YYYY y un número de días,
y luego devuelva la nueva fecha después de sumar esos días.
 Convierte la cadena de fecha en un objeto datetime.
 Usa timedelta para sumar los días a la fecha.
 Muestra la nueva fecha resultante."""

def sumar_dias(fecha, dias):

    fecha_objeto = datetime.strptime(fecha, "%d/%m/%Y")
    nueva_fecha = fecha_objeto + timedelta(days=dias)
    nueva_fecha_formateada = nueva_fecha.strftime("%d/%m/%Y")
    return nueva_fecha_formateada

fecha = "15/11/2024"
dias_a_sumar = 10
nueva_fecha = sumar_dias(fecha, dias_a_sumar)
print("Nueva fecha:", nueva_fecha)


"""Convertir una fecha a otro formato
Crea una función que reciba una fecha en formato YYYY-MM-DD y la convierta en el
formato DD/MM/YYYY.
 Usa strptime para convertir la cadena en un objeto datetime.
 Formatea la fecha en el nuevo formato utilizando strftime."""
from datetime import datetime

def convertir_formato_fecha(fecha):

    fecha_objeto = datetime.strptime(fecha, "%Y-%m-%d")
    
    fecha_formateada = fecha_objeto.strftime("%d/%m/%Y")
    return fecha_formateada

fecha = "2024-11-15"
fecha_convertida = convertir_formato_fecha(fecha)
print("Fecha convertida:", fecha_convertida)
