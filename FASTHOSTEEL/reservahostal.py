from funciones import *

menu_activo=True
opcion_seleccionada= 0
lista_de_reservas=[   
[100, "Usuario", "Juan S", 18000],
[100, "Usuario", "Josefa K", 18000],
[200, "Usuario", "Francisca S", 18000],
[300, "Usuario", "Juan S", 19000],

]
while menu_activo:
    print("Bienvenido al sistema Fast hostel")
    print("Seleccione una opción:")
    print("1.-Guardar una reserva")
    print("2.-Buscar reserva")
    print("3.-Mostrar Reserva")
    print("Modificar Reserva")

    if opcion_seleccionada == 1:
        reserva_modificada=guardar_reserva(lista_de_reservas)
        lista_de_reservas=reserva_modificada
        print("Reserva guardada con éxito")
    if opcion_seleccionada == 2:
        buscar_reserva_por_habitacion(lista_de_reservas)
    
    if opcion_seleccionada == 3:
        mostrar_reserva(lista_de_reservas)

    

