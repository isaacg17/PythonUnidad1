import numpy as np
lista=[1,2,3,4]
arr = np.array(lista)
#print(arr)

#forma 2 directa 
arr2 = np.array([5,6,7,8])
#print(arr2)


#Funcion con arreglo
arreglo= np.array([5,6,7,8,9,10,11,12])
print(arreglo.ndim)

print(arreglo[4:7])
#Arreglo ndim
print(arreglo[0:7:3])

print(arreglo[::2])

#Arreglo a partir de un rango

c = [i for i in range(0,100,1)]
print(c)

#automatizar creacion
x=range(0,5)
arreglo_automatizado= [n for n in x]
print(arreglo_automatizado)
