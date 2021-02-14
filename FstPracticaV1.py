from tkinter import *
from tkinter import filedialog
import re
import os

#Funciones de las opciones en el menu

def File_Upload():
    print("ReadFiles")

def Ordered_List():
    print("ReadFiles")

def Search():
    print("Search")

def Show_All():
    print("All")

def Show_All_Wb():
    print("AllinFile")

def Exit():
    print("Nombre")    

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
        File_Upload()
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
    

