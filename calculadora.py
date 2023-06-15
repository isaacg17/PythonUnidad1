encendido=True
opcion=0






def suma(num_1:int, num_2:int):
    return num_1 + num_2

while encendido:
    print("Bienvenido a la calculadora en python")
    print("1.- Sumar 2 numeros")
    print("2.- Restar 2 numeros")
    print("3.- Multiplicar 2 numeros")
    print("4.- Dividir 2 numeros")  


    opcion=int(input("Seleccione una opcion:"))

if opcion == 1:
    print("Seleccionó :", opcion)
    num_1=int(input("Ingrese el 1er numero"))
    num_2=int(input("Ingrese el 2ndo numero"))
    print(f" {num_1} + {num_2} = {num_1+num_2}")
if opcion == 2:
    print("Seleccionó :", opcion)
if opcion == 3:
    print("Seleccionó :", opcion)
if opcion == 4:
    print("Seleccionó :", opcion)

