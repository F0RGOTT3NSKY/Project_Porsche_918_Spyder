#           _____________________________
#__________/BIBLIOTECAS
import tkinter
from tkinter import *
import time
import threading
#           ____________________________
#__________/VENTANA PRINCIPAL
class Test_Drive_Ventana_Principal:
    def __init__(self, Root_TestDrive, Fondo_TestDrive, Icono_TestDrive, Volante_TestDrive):
        #           ____________________________
        #__________/VARIABLES PRIVADAS
        self.Root_TestDrive = Root_TestDrive
        self.Fondo_TestDrive = Fondo_TestDrive
        self.Icono_TestDrive = Icono_TestDrive
        self.Volante_TestDrive = Volante_TestDrive

        #           ____________________________
        #__________/CONSTRUCTOR DE VENTANA
        Root_TestDrive.title("Formula 1 - ADJ")
        Root_TestDrive.config(bg="white",width=1485,height=900)
        Root_TestDrive.resizable(width=0,height=0)
        Label_Fondo_TestDrive = Label( Root_TestDrive, image = Fondo_TestDrive).place(x=0,y=0)
        Label_Volante = Label( Root_TestDrive,image = Volante_TestDrive).place(x=1202,y=0)
        



#           ____________________________
#__________/VARIABLES GLOBALES
Root = Tk()
Fondo = PhotoImage(file = 'porsche_dash.png')
Icono = Root.iconbitmap('f1logo.ico')
Volante = PhotoImage(file="volante1.png")

#           ____________________________
#__________/INICIAR
Test_Drive_Ventana_Principal(Root, Fondo, Icono, Volante)
Root.mainloop()
