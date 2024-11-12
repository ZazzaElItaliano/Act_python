import re
import json
from datetime import datetime


def cargar_datos(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return json.load(archivo)


def validar_email(email):
    patron_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron_email, email) is not None

def validar_telefono(telefono):
    patron_telefono = r'^[967]\d{8}$' 
    return re.match(patron_telefono, telefono) is not None

def validar_codigo_postal(codigo_postal):
    patron_codigo_postal = r'^\d{5}$'  
    return re.match(patron_codigo_postal, codigo_postal) is not None


def validar_matricula(matricula):
    patron_matricula = r'^\d{4}[A-Za-z]{3}$'  
    return re.match(patron_matricula, matricula) is not None

def validar_ano(ano):
    ano_actual = datetime.now().year
    return 1900 <= ano <= ano_actual

def validar_email_propietario(email):
    patron_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron_email, email) is not None


def validar_alumnos_y_vehiculos(alumnos, vehiculos):
    alumno_correcto=True
    coche_correcto=True
    for alumno in alumnos:
        if not validar_email(alumno["email"]):
            print(f"Email incorrecto para el alumno {alumno['nombre']}")
            alumno_correcto=False
        if not validar_telefono(alumno["telefono"]):
            print(f"Teléfono incorrecto para el alumno {alumno['nombre']}")
            alumno_correcto=False
        if not validar_codigo_postal(alumno["codigo_postal"]):
            print(f"Código postal incorrecto para el alumno {alumno['nombre']}")
            alumno_correcto=False

    for vehiculo in vehiculos:
        if not validar_matricula(vehiculo["matricula"]):
            print(f"Matrícula incorrecta para el vehículo {vehiculo['matricula']}")
            coche_correcto=False
        if not validar_ano(vehiculo["ano"]):
            print(f"Año incorrecto para el vehículo {vehiculo['matricula']}")
            coche_correcto=False
        if not validar_email_propietario(vehiculo["propietario_email"]):
            print(f"Email incorrecto para el propietario del vehículo {vehiculo['matricula']}")
            coche_correcto=False
    return coche_correcto and alumno_correcto


alumnos = cargar_datos('alumnos.json')
vehiculos = cargar_datos('vehiculos.json')


if(validar_alumnos_y_vehiculos(alumnos, vehiculos)):
    print("Todos los datos de alumnos y coches son correctos")

