def ordenamientoBurbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp
    
    return unaLista

unaLista = [123,123,6546,545,7,8]
casa = ordenamientoBurbuja(unaLista)
print(casa)
print("11")

#Ordenamiento De Burbuja: compara cada elemento de la lista de valores para irlos ordenando uno por uno

Lista = [123,123,6546,545,7,8]
bandera = False

while bandera == False:
    bandera = True
    for i in range(len(Lista)-1): #recorre la lista menos uno para que cabal compare el penultimo con el ultimo
        if Lista[i] > Lista[i+1]: #condiciona los elementos para que se realice el cambio de ordenamiento
            contenedor = Lista[i]
            Lista[i] = Lista[i+1]
            Lista[i+1] = contenedor
            bandera = False #verifica que ya no hayan elementos desordenados para terminar el ciclo

print(Lista)
print("2")


#Ordenamiento por seleccion: Se basa en la seleccion de los valores maximos y minimos
def Ordenamiento_Selectivo(Lista_a_Ordenar):
    for i in range(len(Lista_a_Ordenar)):#se encarga de ordenar los elementos
        Elemento_Menor = i
        for j in range(i+1, len(Lista_a_Ordenar)):
            if Lista_a_Ordenar[j] < Lista_a_Ordenar[Elemento_Menor]:
                Elemento_Menor = j

        Cambio(Lista_a_Ordenar, Elemento_Menor, i)

def Cambio(A, x, y):# hace el cambio entre elementos
    contenedor4 = A[x]
    A[x]=A[y]
    A[y]= contenedor4

Lista = [5.76,4.7,25.3,4.6,32.4,55.3,52.3,7.6,7.3,86.7,43.5]
Ordenamiento_Selectivo(Lista)
print(Lista)



#metodo para buscar el elmento
#test_list = [[1, 54, 7, 2, 7, 7, 5, 7], [4, 5, 5, 2], [10, 5, 10, 5]] 
#array_original = []
#CONTADOR = 0
#
#for i in range(len(test_list)): #For para obtener los arrays internos-tamaño 3
#    Lista_Interna = test_list[i]
#    DIM = len(Lista_Interna)
#    List_index = []
#
#    for j in range(DIM):    #for para obtener los numeros y compararlos
#        if Lista_Interna[j] == 5:
#            List_index.append(j)
#    array_original.append(List_index)
#
#print(array_original)






#-------------------------------------------------------------------------------------------------------------------------------------
##Funcion Para Realizar el ordenamiento de las listas
##-------------------------------------------------------------------------------------------------------------------------------------
#def Ordenamiento(Lista):
#    bandera = False
#
#    while bandera == False:
#        bandera = True
#        for i in range(len(Lista)-1): #recorre la lista menos uno para que cabal compare el penultimo con el ultimo
#            if Lista[i] > Lista[i+1]: #condiciona los elementos para que se realice el cambio de ordenamiento
#                contenedor = Lista[i]
#                Lista[i] = Lista[i+1]
#                Lista[i+1] = contenedor
#                bandera = False #verifica que ya no hayan elementos desordenados para terminar el ciclo
#
#    return Lista    #Devuelve la LINEA ordenada
#
#
##-------------------------------------------------------------------------------------------------------------------------------------
##Funcion Para Realizar la busqueda en las listas
##-------------------------------------------------------------------------------------------------------------------------------------
def Selective_Search(test_list, buscar): 
    array_original = []
    Contador_Linea_Encuentro = 1

    for i in range(len(test_list)): #For para obtener los arrays internos-tamaño 3
        Lista_Interna = test_list[i]
        DIM = len(Lista_Interna)
        List_index = []

        for j in range(DIM):    #for para obtener los numeros y compararlos
            if Lista_Interna[j] == buscar:
                List_index.append(j)
            array_original.append(List_index)

    return array_original      #Devuelve un array con la busqueda de todas las lineas en general

