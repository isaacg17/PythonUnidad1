import numpy as np
import re
import random

#Defino vehiculo
class Vehiculo: #class encapsula datos
    def __init__(self, tipo, patente, marca, precio, multas, fecha_registro, dueno):
        self.tipo = tipo
        self.patente = patente
        self.marca = marca
        self.precio = precio
        self.multas = multas
        self.fecha_registro = fecha_registro
        self.dueno = dueno

#Mostrar informacion vehiculo
    def mostrar_informacion(self): 
        print("Tipo:", self.tipo)
        print("Patente:", self.patente)
        print("Marca:", self.marca)
        print("Precio:", self.precio)
        print("Multas:", self.multas)
        print("Fecha de registro:", self.fecha_registro)
        print("Dueño:", self.dueno)

#Validacion
def validar_patente(patente):
    # Expresión regular para verificar patentes chilenas (tuve que buscar un patron de patente obviamente)
    patron = r'^[A-Z]{2}\d{2}[A-Z]{2}$'
    return re.match(patron, patente) is not None

#Grabacion de vehiculos

def grabar_vehiculo(vehiculos):
    tipo = input("Ingrese el tipo de vehículo: ")
    patente = input("Ingrese la patente del vehículo: ")

    while not validar_patente(patente):
        print("La patente ingresada no es válida. Ejemplo de formato válido: AB12CD")
        patente = input("Ingrese la patente del vehículo: ")

    marca = input("Ingrese la marca del vehículo: ")
    precio = int(input("Ingrese el precio del vehículo: "))


#Precio mayor a 5 millions
    while precio <= 5000000:
        print("El precio debe ser mayor a $5.000.000")
        precio = int(input("Ingrese el precio del vehículo: "))


#Ingreso de multaas

    multas = []
    opcion = input("Desea ingresar una multa? (S/N): ")

    while opcion.upper() == "S":
        monto = float(input("Ingrese el monto de la multa: "))
        fecha = input("Ingrese la fecha de la multa: ")
        multas.append((monto, fecha))
        opcion = input("Desea ingresar otra multa? (S/N): ")

    fecha_registro = input("Ingrese la fecha de registro del vehículo: (xx-xx-xx) ")
    dueno = input("Ingrese el nombre y apellido del dueño del vehículo: ")

    vehiculo = Vehiculo(tipo, patente, marca, precio, multas, fecha_registro, dueno)
    vehiculos.append(vehiculo)
    print("Vehículo grabado correctamente.")

#Buscar
def buscar_vehiculo(vehiculos):
    patente = input("Ingrese la patente del vehículo que desea buscar: ")
    encontrado = False

    for vehiculo in vehiculos:
        if vehiculo.patente == patente:
            vehiculo.mostrar_informacion()
            encontrado = True
            break

    if not encontrado:
        print("No se encontró un vehículo con esa patente, Reintenta nuevamente.")

#Impresion de certificados.

def imprimir_certificados(vehiculos):
    for vehiculo in vehiculos:
        print("Certificado de Emisión de contaminantes")
        print("Nombre del certificado: Emisión de contaminantes")
        print("Patente del auto:", vehiculo.patente)
        print("Datos del dueño:", vehiculo.dueno)
        print()

        print("Certificado de anotaciones vigentes")
        print("Nombre del certificado: Anotaciones vigentes")
        print("Patente del auto:", vehiculo.patente)
        print("Datos del dueño:", vehiculo.dueno)
        print()


def main():
    vehiculos = []

#Menú con sus correspondientes opciones
    while True:
        print("----- MENÚ -----")
        print("1. Grabar vehículo")
        print("2. Buscar vehículo")
        print("3. Imprimir certificados")
        print("4. Salir del menú")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            grabar_vehiculo(vehiculos)
        elif opcion == 2:
            buscar_vehiculo(vehiculos)
        elif opcion == 3:
            imprimir_certificados(vehiculos)
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    print("Bienvenido(a) a Auto Seguro - Versión Beta 1.0")
    print("Desarrollado por Isaac Gomez")
    print()
    main()
