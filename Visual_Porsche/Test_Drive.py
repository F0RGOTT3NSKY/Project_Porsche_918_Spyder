#           _____________________________
#__________/BIBLIOTECAS
import tkinter
from tkinter import *
import time
import threading

           
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
Emergency = PhotoImage(file="emergencia_mini.png")
Headlights_Off = PhotoImage(file="off.png")
Headlights_On = PhotoImage(file="on.png")



#           ____________________________
#__________/VENTANA PRINCIPAL
class Test_Drive_Ventana_Principal:
    def __init__(self, Root_TestDrive, Fondo_TestDrive, Icono_TestDrive, Volante_TestDrive,
                 Dir_Izq_Default_TestDrive, Dir_Der_Default_TestDrive, Pedal_Clutch_TestDrive,
                 Pedal_Break_TestDrive, Pedal_Accelerator_TestDrive, Palanca_Dir_Izq_TestDrive,
                 Palanca_Dir_Der_TestDrive, Emergency_TestDrive, Headlights_Off_TestDrive,
                 Headlights_On_TestDrive):
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
        self.Emergency_TestDrive = Emergency_TestDrive
        self.Headlights_Off_TestDrive = Headlights_Off_TestDrive
        self.Headlights_On_TestDrive = Headlights_On_TestDrive
        
        
        #           ____________________________
        #__________/CONSTRUCTOR DE VENTANA
        Root_TestDrive.title("Formula 1 - ADJ")
        Root_TestDrive.config(bg="black",width=1485,height=800)
        Root_TestDrive.resizable(width=0,height=0)
        
        Label_Fondo_TestDrive = Label( Root_TestDrive, image = Fondo_TestDrive).place(x=0,y=0)
        Label_Volante = Label( Root_TestDrive,image = Volante_TestDrive).place(x=1202,y=0)
        Label_Dir_Izq_Default = Label( Root_TestDrive, image = Dir_Izq_Default_TestDrive).place(x=1202,y=500)
        Label_Dir_Der_Default = Label( Root_TestDrive, image = Dir_Der_Default_TestDrive).place(x=1340,y=500)

        Button_Pedal_Clutch_TestDrive = Button( Root_TestDrive, image = Pedal_Clutch_TestDrive).place(x=245,y=440)
        Button_Pedal_Break_TestDrive = Button( Root_TestDrive, image = Pedal_Break_TestDrive).place(x=400,y=440)
        Button_Pedal_Accelerator_TestDrive = Button( Root_TestDrive, image = Pedal_Accelerator_TestDrive).place(x=514,y=440)
        Button_Palanca_Dir_Izq_TestDrive = Button( Root_TestDrive, image = Palanca_Dir_Izq_TestDrive).place(x=275,y=298)
        Button_Palanca_Dir_Der_TestDrive = Button( Root_TestDrive, image = Palanca_Dir_Der_TestDrive).place(x=515,y=298)
        Button_Emergency_TestDrive = Button( Root_TestDrive, image = Emergency_TestDrive).place(x=420,y=370)
        Button_Headlights_On_TestDrive1 = Button( Root_TestDrive, image = Headlights_On_TestDrive, command = self.Frontales_Off).place(x=1202,y=280)
        Button_Headlights_Off_TestDrive = Button( Root_TestDrive, image = Headlights_Off_TestDrive, command = self.Frontales_On).place(x=1202,y=280)
        
        
       
        
        Root_TestDrive.mainloop()
        
        #           ____________________________
        #__________/LUCES FRONTALES
    def Frontales_On(self):
        print("Headlights On")
        Button_Headlights_On_TestDrive = Button( self.Root_TestDrive, image = self.Headlights_On_TestDrive, command = self.Frontales_Off).place(x=1202,y=280)
       
    def Frontales_Off(self):
        print("Headlights Off")
        Button_Headlights_Off_TestDrive = Button( self.Root_TestDrive, image = self.Headlights_Off_TestDrive, command = self.Frontales_On).place(x=1202,y=280)
        
#           ____________________________
#__________/INICIAR
Test_Drive_Ventana_Principal(Root, Fondo, Icono, Volante, Dir_Izq_Default, Dir_Der_Default,
                             Pedal_Clutch, Pedal_Break, Pedal_Accelerator, Palanca_Dir_Izq,
                             Palanca_Dir_Der, Emergency, Headlights_Off, Headlights_On)
Root.mainloop()
