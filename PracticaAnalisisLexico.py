from tkinter import *
from tkinter import filedialog
import re

#Abre y lee el txt linea por linea almacenando en Array_List
root = Tk().withdraw()

File_Route = filedialog.askopenfilename()   
Open_File = open(File_Route , "r")
Array_Lines = []
Array_Lines = Open_File.readlines()
Dm = len(Array_Lines)

Open_File.close()

def Analyze_File(File_Line, Dml):
  Array_Id = []
  Array_NumList_Temp = []
  Array_NumList_clr = []
  Array_Reserved_Word_clr = []
  Array_Reserved_Word_Temp = []
  Array_Number_to_Search = []
  Line_Counter = 0
  Len_Line_Reserved_Word = 0

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
  
  return Array_Id, Array_Reserved_Word_clr, Array_NumList_clr

#Arreglo de listado y salida del txt
  for i in range(Dml):
    Line_Counter += 1
    Line_Reserved_Words = Array_Reserved_Word_clr[i]
    Len_Line_Reserved_Word = len(Array_Reserved_Word_clr[i])

    if Len_Line_Reserved_Word == 1:
      if Line_Reserved_Words[0] == "BUSCAR": #validar las dimensiones para determinar el valor a buscar
        Line_Array_NumList = Array_NumList_clr[i]
        Abuscar = Line_Array_NumList[-1]
#aca le agregue la linea para almacenar los valores a buscar en un array para que lo busque bien paro nose que me imprime
        Array_Number_to_Search.append(Abuscar)
#--------------------------------------------------------------------------------------------------------------------------
        Eliminacion_Numero_Buscar =  Array_NumList_clr[i]
        del Eliminacion_Numero_Buscar[-1]

        print("------------------------------------------------------")
        print("                Linea_Numero = ", Line_Counter)
        print("------------------------------------------------------")
        print("Identificador = ", Array_Id[i])
        print("Lista_Numeros = ", Array_NumList_clr[i])
        print("Palabras_Reservadas = ", Array_Reserved_Word_clr[i])
        print("Valor_a_Buscar = ", Abuscar)
        print("")
      
      else:
        print("------------------------------------------------------")
        print("               Linea_Numero = ", Line_Counter)
        print("------------------------------------------------------")
        print("Identificador = ", Array_Id[i])
        print("Lista_Numeros = ", Array_NumList_clr[i])
        print("Palabras_Reservadas = ", Array_Reserved_Word_clr[i])
        print("")

    else:
      if Line_Reserved_Words[1] == "BUSCAR": #validar las dimensiones para determinar el valor a buscar
        Line_Array_NumList = Array_NumList_clr[i]
        Abuscar = Line_Array_NumList[-1]
        Eliminacion_Numero_Buscar =  Array_NumList_clr[i]
        del Eliminacion_Numero_Buscar[-1]

        print("------------------------------------------------------")
        print("                Linea_Numero = ", Line_Counter)
        print("------------------------------------------------------")
        print("Identificador = ", Array_Id[i])
        print("Lista_Numeros = ", Array_NumList_clr[i])
        print("Palabras_Reservadas = ", Array_Reserved_Word_clr[i])
        print("Valor_a_Buscar = ", Abuscar)
        print("")
      else:
        print("------------------------------------------------------")
        print("                Linea_Numero = ", Line_Counter)
        print("------------------------------------------------------")
        print("Identificador = ", Array_Id[i])
        print("Lista_Numeros = ", Array_NumList_clr[i])
        print("Palabras_Reservadas = ", Array_Reserved_Word_clr[i])
        print("")




listaaaaaa = Analyze_File(Array_Lines, Dm)
for i in range(len(listaaaaaa)):
  print (listaaaaaa[i])
  print("")

