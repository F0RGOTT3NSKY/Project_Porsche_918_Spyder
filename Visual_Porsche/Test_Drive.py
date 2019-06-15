#           _____________________________
#__________/BIBLIOTECAS
import tkinter
from tkinter import *
import time
import threading
#           ____________________________
#__________/VENTANA PRINCIPAL
class Test_Drive_Ventana_Principal:
    def __init__(self, Root_TestDrive, Fondo_TestDrive, Icono_TestDrive, Volante_TestDrive,
                 Dir_Izq_Default_TestDrive, Dir_Der_Default_TestDrive, Pedal_Clutch_TestDrive,
                 Pedal_Break_TestDrive, Pedal_Accelerator_TestDrive, Palanca_Dir_Izq_TestDrive,
                 Palanca_Dir_Der_TestDrive):
        #           ____________________________
        #__________/VARIABLES PRIVADAS
        self.Root_TestDrive = Root_TestDrive
        self.Fondo_TestDrive = Fondo_TestDrive
        self.Icono_TestDrive = Icono_TestDrive
        self.Volante_TestDrive = Volante_TestDrive
        self.Dir_Izq_Default_TestDrive = Dir_Izq_Default_TestDrive
        self.Dir_Der_Default_TestDrive = Dir_Der_Default_TestDrive
        self.Pedal_Clutch_TestDrive = Pedal_Clutch_TestDrive
        self.Pedal_Break_TestDrive = Pedal_Break_TestDrive
        self.Pedal_Accelerator_TestDrive = Pedal_Accelerator_TestDrive
        self.Palanca_Dir_Izq_TestDrive = Palanca_Dir_Izq_TestDrive
        self.Palanca_Dir_Der_TestDrive = Palanca_Dir_Der_TestDrive

        #           ____________________________
        #__________/CONSTRUCTOR DE VENTANA
        Root_TestDrive.title("Formula 1 - ADJ")
        Root_TestDrive.config(bg="white",width=1485,height=800)
        Root_TestDrive.resizable(width=0,height=0)
        
        Label_Fondo_TestDrive = Label( Root_TestDrive, image = Fondo_TestDrive).place(x=0,y=0)
        Label_Volante = Label( Root_TestDrive,image = Volante_TestDrive).place(x=1202,y=0)
        Label_Dir_Izq_Default = Label( Root_TestDrive, image = Dir_Izq_Default_TestDrive).place(x=1202,y=500)
        Label_Dir_Der_Default = Label( Root_TestDrive, image = Dir_Der_Default_TestDrive).place(x=1340,y=500)

        Button_Pedal_Clutch_TestDrive = Button( Root_TestDrive, image = Pedal_Clutch_TestDrive).place(x=245,y=440)
        Button_Pedal_Break_TestDrive = Button( Root_TestDrive, image = Pedal_Break_TestDrive).place(x=400,y=440)
        Button_Pedal_Accelerator_TestDrive = Button( Root_TestDrive, image = Pedal_Accelerator_TestDrive).place(x=514,y=440)
        Button_Palanca_Dir_Izq_TestDrive = Button( Root_TestDrive, image = Palanca_Dir_Izq_TestDrive, command=lambda :thread_direccion_izquierda()).place(x=275,y=298)
        Button_Palanca_Dir_Der_TestDrive = Button( Root_TestDrive, image = Palanca_Dir_Der_TestDrive, command=lambda :thread_direccion_derecha()).place(x=515,y=298)
#           ____________________________
#__________/VARIABLES GLOBALES
Root = Tk()
Fondo = PhotoImage(file = 'porsche_dash.png')
Icono = Root.iconbitmap('f1logo.ico')
Volante = PhotoImage(file="volante1.png")
Dir_Izq_Default = PhotoImage(file="direccion_izquierda_default.png")        
Dir_Der_Default = PhotoImage(file="direccion_derecha_default.png")
Pedal_Clutch = PhotoImage(file="pedal.png")
Pedal_Break = PhotoImage(file="freno.png")
Pedal_Accelerator = PhotoImage(file="gas.png")
Palanca_Dir_Izq = PhotoImage(file="direccional.png")
Palanca_Dir_Der = PhotoImage(file="direccional_derecha.png")
#           ____________________________
#__________/INICIAR
Test_Drive_Ventana_Principal(Root, Fondo, Icono, Volante, Dir_Izq_Default, Dir_Der_Default,
                             Pedal_Clutch, Pedal_Break, Pedal_Accelerator, Palanca_Dir_Izq,
                             Palanca_Dir_Der)
Root.mainloop()
