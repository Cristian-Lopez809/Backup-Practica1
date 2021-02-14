from tkinter import *
from tkinter import filedialog
import re

#-------------------------------------------------------------------------------------------------------------------------------------
#Funcion Para Cargar las lineas completas
#-------------------------------------------------------------------------------------------------------------------------------------
root = Tk().withdraw()

File_Route = filedialog.askopenfilename()   
Open_File = open(File_Route , "r")
Array_Lines = []
Array_Lines = Open_File.readlines()
Dm = len(Array_Lines)

Open_File.close()


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


#Saco por medio del return del metodo analizador - los id, numeros, preservadas en arrays
listaaaaaa = Analyze_File(Array_Lines, Dm)
for i in range(len(listaaaaaa)):
  print (listaaaaaa[i])
  print("")


