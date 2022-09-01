#Problema del morral:
#Consiste en un algoritmo que determina cuantos paquetes de un asignado valor
#entrarían en una mochila con una capacidad declarada
#Se emplea recursividad para solventar el código.

def mochila(tamano,peso,valor,n):
    #comenzamos definiendo la funcion recursiva
    
    if n == 0 or tamano == 0 :
        return 0
    #caso base
    
    if peso[n-1] > tamano:
        return mochila(tamano,peso,valor,n-1)
    #caso base alternativo
    
    return max(valor[n-1] + mochila(tamano - peso[n-1], peso,valor,n-1), mochila(tamano,peso,valor,n-1))
    #retorna el valor maximo comparando su posicion en N tomando ese valor 
    #y considerando sino el proximo valor



if __name__=="__main__":
    #se entregan dos arrays, correlacionados entre si
    pesaje = [20,30,60]
    valores = [100,200,300]
    n = len(pesaje)
    BagSize = 40
    #BagSize es la variable del tamano del morral, en base al pesaje
    #se determinan los paquetes que entran y su valor maximo posible
    
    print(mochila(BagSize,pesaje,valores,n))
