from tkinter import *
from tkinter import filedialog
import re


#-------------------------------------------------------------------------------------------------------------------------------------
#Funcion Para Cargar las lineas completas
#-------------------------------------------------------------------------------------------------------------------------------------
def Upload():
  root = Tk().withdraw()

  File_Route = filedialog.askopenfilename()   
  Open_File = open(File_Route , "r")
  Array_Lines = []
  Array_Lines = Open_File.readlines()
  Dm = len(Array_Lines)

  Open_File.close()
  return Array_Lines, Dm

#-------------------------------------------------------------------------------------------------------------------------------------
#FUNCION PARA ANALIZAR LOS DATOS
#-------------------------------------------------------------------------------------------------------------------------------------
def Analyze_File(File_Line, Dml):
  Array_Id = []
  Array_NumList_Temp = []
  Array_NumList_clr = []
  Array_Reserved_Word_clr = []
  Array_Reserved_Word_Temp = []
  Array_Number_to_Search = []
  Line_Counter = 0
  LenReservadas = 0

  # Bucle para obtener los ID
  for i in range(Dml):
    Contenedor = File_Line[i].split("=")
    Array_Id.append(Contenedor[0])
  
  #For para obtener las palabras reservadas
  for i in range(Dml):
    Contenedor = File_Line[i].split("=")
    Array_Reserved_Word_Temp.append(Contenedor[1])
    Array_Reserved_Word_clr.append(re.findall(r"\w[a-zA-Z]+", Array_Reserved_Word_Temp[i]))

  #For para obtener las listas de numeros
  for i in range(Dml):
    Contenedor = File_Line[i].split("=")
    Array_NumList_Temp.append(Contenedor[1])
    Array_NumList_clr.append(re.findall("\d{1,}", Array_NumList_Temp[i]))

#Se encarga de validar si se esta buscando algun numero y si si lo elimina de la lista para dejarlo perfecto
  for i in range(Dml):
    Line_Counter += 1
    Line_Reserved_Words = Array_Reserved_Word_clr[i]
    Len_Line_Reserved_Word = len(Array_Reserved_Word_clr[i])

    if Len_Line_Reserved_Word == 1: #validar las dimensiones para determinar el valor a buscar
      if Line_Reserved_Words[0] == "BUSCAR": #si en el espacio 0 esta buscar
        Line_Array_NumList = Array_NumList_clr[i]
        Abuscar = Line_Array_NumList[-1]
#aca le agregue la linea para almacenar los valores a buscar en un array para que lo busque bien paro nose que me imprime
        Array_Number_to_Search.append(Abuscar)
        Eliminacion_Numero_Buscar =  Array_NumList_clr[i]
        del Eliminacion_Numero_Buscar[-1]
    else:       #valida QUE HAY MAS DE DOS ELEMENTOS EN RESERVADAS
      if Line_Reserved_Words[1] == "BUSCAR": #VALIDA QUE ESTE EL BUSCAR EN LA SEGUNDA POSICION 
        Line_Array_NumList = Array_NumList_clr[i]
        Abuscar = Line_Array_NumList[-1]
#aca le agregue la linea para almacenar los valores a buscar en un array para que lo busque bien paro nose que me imprime
        Array_Number_to_Search.append(Abuscar)
        Eliminacion_Numero_Buscar =  Array_NumList_clr[i]
        del Eliminacion_Numero_Buscar[-1]

  return Array_Id, Array_Reserved_Word_clr, Array_NumList_clr, Array_Number_to_Search, Line_Counter

#-------------------------------------------------------------------------------------------------------------------------------------
#Funcion Para Realizar el ordenamiento de las listas
#-------------------------------------------------------------------------------------------------------------------------------------
def Ordenamiento(Ordered_List):
  Lista_enteros = []
  Bandera = False

  for i in range(len(Ordered_List)):
    Lista_enteros.append(int(Ordered_List[i])) 

  while Bandera == False:
      Bandera = True
      for i in range(len(Lista_enteros)-1): #recorre la Ordered_List 
          if Lista_enteros[i] > Lista_enteros[i+1]: #condiciona los elementos para que se realice el cambio de ordenamiento
              Contenedor_Temp = Lista_enteros[i]
              Lista_enteros[i] = Lista_enteros[i+1]
              Lista_enteros[i+1] = Contenedor_Temp
              Bandera = False 

  return Lista_enteros    #Linea Ordenada

#-------------------------------------------------------------------------------------------------------------------------------------
#Funcion De Busqueda en la lista
#-------------------------------------------------------------------------------------------------------------------------------------
def Selective_Search(test_list, Buscar):
  array_original = []
  DIM = len(test_list)
  List_index = []

  for i in range(DIM):    #for para obtener los numeros y compararlos
    if test_list[i] == Buscar:
      List_index.append(i)

  if List_index == []:
    array_original = "**NO ENCONTRADA**"
  else:
    array_original = List_index

  return array_original     #Devuelve un array con la busqueda de todas las lineas en general
