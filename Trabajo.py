import numpy as np
import random



#funcion con argumento y sin retorno

def resta1(num_1,num_2):
    resultado=num_1-num_2
    print("El resultado de la resta es:", resultado)

resta1(10,1)
def resta2(num_1, num_2):
    resultado=num_1-num_2
    return resultado

resultado_1=resta1(10,1)#9
resultado_2=resta2(0,3)#5
#labuena
print(resultado_1-resultado_2)


