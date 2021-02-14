#Ordenamiento De Burbuja: compara cada elemento de la lista de valores para irlos ordenando uno por uno

Lista = [123,1,5,78,2,45]
bandera = False
bandera2 = False

while bandera == False:
    bandera = True
    for i in range(len(Lista)-1): #recorre la lista menos uno para que cabal compare el penultimo con el ultimo
        if Lista[i] > Lista[i+1]: #condiciona los elementos para que se realice el cambio de ordenamiento
            contenedor = Lista[i]
            Lista[i] = Lista[i+1]
            Lista[i+1] = contenedor
            bandera = False #verifica que ya no hayan elementos desordenados para terminar el ciclo

print(Lista)



#Ordenamiento por seleccion: Se basa en la seleccion de los valores maximos y minimos

print("*******************************************************************************************")
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


#Algoritmo de Busqueda lineal: Se busca en cada elemento de la lista hasta encontrar el que se quiere

print("*******************************************************************************************")

def Busqueda_Lineal(Abuscar, ListaNueva):
    Encontrado = False
    Dim = len(ListaNueva) 
    Lista_Almacenamiento = []

    for i in range(Dim):    #for para buscar y almacenar posiciones
        if ListaNueva[i] == Abuscar:
            Lista_Almacenamiento.append(Lista.index(Abuscar)+1)
            Encontrado = True
        else:
            return Encontrado

    if Encontrado != False:
        print("Los elementos encontrados estan en las posiciones:")
        for i in range(len(Lista_Almacenamiento)):   #For para mostrar posicion de encuentro o si no hay nada
            #iba a validar que estuviera llena pero creo que no es necesario-----if Lista_Almacenamiento[i] != None:
            print(Lista_Almacenamiento[i], end="")  # el end lo puedo omitir en caso no funcione luego
            # aca iba un sino con un break por si el espacio fuera nulo, pero creo que no es necesario
    else:
        print("ELEMENTO NO ECONTRADO")

Lista48 = [5,47,25,4,7,43]
Busqueda_Lineal(25, Lista48)





#metodo para buscar el elmento
test_list = [[1, 54, 7, 2, 7, 7, 5, 7], [4, 5, 5, 2], [10, 5, 10, 5]] 
array_original = []
CONTADOR = 0

for i in range(len(test_list)): #For para obtener los arrays internos-tamaño 3
    Lista_Interna = test_list[i]
    DIM = len(Lista_Interna)
    List_index = []

    for j in range(DIM):    #for para obtener los numeros y compararlos
        if Lista_Interna[j] == 5:
            List_index.append(j)
    array_original.append(List_index)

print(array_original)
#print(array_original)


