def guardar_reserva(lista_de_reservas):
    print("Seleccionó Opcion 1")
    cantidad_personas=int(input("Ingrese la cantidad de personas"))
    habitacion=int("Ingrese la habitacion")
    nombre_reserva=input("Ingrese la habitacion")
    nombre_pasajero=input("Ingrese el nombre del pasajero")
    lista_de_reservas.append()
    precio=cantidad_personas*10000

    for n_persona in range(cantidad_personas):
        nombre_pasajero=input("Ingrese el nombre del pasajero")
        lista_de_reservas.append(habitacion,nombre_reserva,nombre_pasajero,precio)
    return lista_de_reservas


def buscar_reserva_por_habitacion(lista_de_reservas):
    print("Seleccionó la opcion 2")
    habitacion_buscada=int(input("Ingrese nombre de habitacion"))
    largo_lista=len(lista_de_reservas)

    for fila in range(largo_lista):
        print(lista_de_reservas)

def mostrar_reserva(lista_de_reservas):
    print("Seleccionó la opcion 3")


