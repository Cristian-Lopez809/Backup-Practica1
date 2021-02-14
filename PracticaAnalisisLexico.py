from tkinter import *
from tkinter import filedialog
import re

root = Tk().withdraw()

File_Route = filedialog.askopenfilename()   #Abre y lee el txt linea por linea almacenando en Array_List
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
  ContadorLinea = 0
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

#Arreglo de listado y salida del txt
  for i in range(Dml):
    ContadorLinea += 1
    Palabra_Search = Array_Reserved_Word_clr[i]
    LenReservadas = len(Array_Reserved_Word_clr[i])

    if LenReservadas == 1:
      if Palabra_Search[0] == "BUSCAR": #validar las dimensiones para determinar el valor a buscar
        contenedor = Array_NumList_clr[i]
        Abuscar = contenedor[-1]
        eliminacion =  Array_NumList_clr[i]
        del eliminacion[-1]

        print("------------------------------------------------------")
        print("                Linea_Numero = ", ContadorLinea)
        print("------------------------------------------------------")
        print("Identificador = ", Array_Id[i])
        print("Lista_Numeros = ", Array_NumList_clr[i])
        print("Palabras_Reservadas = ", Array_Reserved_Word_clr[i])
        print("Valor_a_Buscar = ", Abuscar)
        print("")
      
      else:
        print("------------------------------------------------------")
        print("               Linea_Numero = ", ContadorLinea)
        print("------------------------------------------------------")
        print("Identificador = ", Array_Id[i])
        print("Lista_Numeros = ", Array_NumList_clr[i])
        print("Palabras_Reservadas = ", Array_Reserved_Word_clr[i])
        print("")

    else:
      if Palabra_Search[1] == "BUSCAR": #validar las dimensiones para determinar el valor a buscar
        contenedor = Array_NumList_clr[i]
        Abuscar = contenedor[-1]
        eliminacion =  Array_NumList_clr[i]
        del eliminacion[-1]

        print("------------------------------------------------------")
        print("                Linea_Numero = ", ContadorLinea)
        print("------------------------------------------------------")
        print("Identificador = ", Array_Id[i])
        print("Lista_Numeros = ", Array_NumList_clr[i])
        print("Palabras_Reservadas = ", Array_Reserved_Word_clr[i])
        print("Valor_a_Buscar = ", Abuscar)
        print("")
      else:
        print("------------------------------------------------------")
        print("                Linea_Numero = ", ContadorLinea)
        print("------------------------------------------------------")
        print("Identificador = ", Array_Id[i])
        print("Lista_Numeros = ", Array_NumList_clr[i])
        print("Palabras_Reservadas = ", Array_Reserved_Word_clr[i])
        print("")

Analyze_File(Array_Lines, Dm)