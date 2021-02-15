from tkinter import *
from tkinter import filedialog
import re
import os
from Funciones import *

#Variables de acceso a las funciones
Reading_Array = []
General_container = []
Array_Listas_Ordenadas = []
Array_Listado_Buscados = []
Encontrado_En = []
Contador_Linea = 0


#Funciones del Menu
def File_Upload():
    Read_File = Upload()
    return Read_File

def Ordered_List():
    Contador_Linea = General_container[4]
    Auxiliar_Listas_Numeros = General_container[2]

    for i in range(len(Auxiliar_Listas_Numeros)):
        Linea_ListaNumerica = Auxiliar_Listas_Numeros[i]
        Linea_lista_ordenada = Ordenamiento(Linea_ListaNumerica)
        Array_Listas_Ordenadas.append(Linea_lista_ordenada)
    
    print("-------------------------------------     Listas Ordenadas     -------------------------------------")
    for i in range(Contador_Linea):
        print("         Lista Ordenada No.", i+1, ":  ", Array_Listas_Ordenadas[i])
        print("")

def Search():
    Array_Aux_ListNum = General_container[2] 
    Array_Aux_ListSearched = General_container[3]
    Array_Aux_ReservedWords = General_container[1]
    Numero_Lineas = General_container[4]
    Iterador_Buscados = 0 # Iterador_Buscados QUE SE ENCARGA DE RECORRER EL LISTADO DE PALABRAS RESERVADAS 

    for i in range(Numero_Lineas):#for que me permite saber en que linea estoy
        Linea_N_PalabrasReservadas = Array_Aux_ReservedWords[i]

        if len(Linea_N_PalabrasReservadas) == 1: #Se determina la dimension de cada linea 
            if Linea_N_PalabrasReservadas[0] == "BUSCAR":
                Array_Listado_Buscados.append(Selective_Search(Array_Aux_ListNum[i], Array_Aux_ListSearched[Iterador_Buscados]))
                Iterador_Buscados += 1
                Encontrado_En.append(i)
        else:
            if Linea_N_PalabrasReservadas[1] == "BUSCAR": 
                Array_Listado_Buscados.append(Selective_Search(Array_Aux_ListNum[i], Array_Aux_ListSearched[Iterador_Buscados]))
                Iterador_Buscados += 1
                Encontrado_En.append(i)

    #Imprimiendo las salidas
    print("-------------------------------------     Resultados de Busqueda      -------------------------------------")
    for i in range(len(Encontrado_En)):
        print("Numero a buscar: {", Array_Aux_ListSearched[i],"} Encontrado en la/s posición: ", Array_Listado_Buscados[i], ". De la lista No.", Encontrado_En[i]+1, ": ", Array_Aux_ListNum[Encontrado_En[i]])
        print("")

def Show_All():
    Array_Aux_ListSearched = General_container[3]
    Array_Aux_ListNum = General_container[2]
    Contador_Linea = General_container[4] 

    print("------------------------     Listas Ordenadas     ------------------------")
    print("")

    for i in range(Contador_Linea):
        print("         Lista No.", i+1, ":  ", Array_Listas_Ordenadas[i])
        print("")

    print("")
    print("-------------------------------------     Resultados de Busqueda      -------------------------------------")
    print("")

    for i in range(len(Encontrado_En)):
        print("Numero a buscar: {", Array_Aux_ListSearched[i],"} Encontrado en la/s posición: ", Array_Listado_Buscados[i], ". De la lista No.", Encontrado_En[i]+1, ": ", Array_Aux_ListNum[Encontrado_En[i]])
        print("")

def Show_All_Wb():
    print("AllinFile")

def Exit():
    print("Nombre")  

def Analyze_General(Doc_Leido):
    Lineas = Doc_Leido[0]
    Tamaño = Doc_Leido[1]
    #Saco por medio del return del metodo analizador - los id, numeros, preservadas en arrays
    Contendedor_General = Analyze_File(Lineas, Tamaño)
    
    return Contendedor_General  


while True:
    print("-------------------------------------------------------")
    print("                   MENÚ PRINCIPAL")
    print("-------------------------------------------------------")
    print("")
    print("     1- Cargar un Archivo.")
    print("     2- Desplegar Listas Ordenadas.")
    print("     3- Desplegar Busquedas.")
    print("     4- Desplegar Todas.")
    print("     5- Desplegar Todas a Archivos.")
    print("     6- Salir.")
    print("")

    Accion = int(input("Escoje una opción:  \n\
    -------->   "))
    print("")

    if Accion == 1:
        Reading_Array = File_Upload()
        General_container =  Analyze_General(Reading_Array)
    elif Accion == 2:
        Ordered_List()
    elif Accion == 3:
        Search()
    elif Accion == 4:
        Show_All()
    elif Accion == 5:
        Show_All_Wb()
    elif Accion == 6:
        Exit()
        #evento de botton que contendra al break
        break
        
    input()
    os.system("cls")
    

