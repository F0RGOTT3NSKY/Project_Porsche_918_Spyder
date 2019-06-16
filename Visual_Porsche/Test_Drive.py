#           _____________________________
#__________/BIBLIOTECAS
import tkinter
from tkinter import *
import time
import threading
from threading import *

           
#           ____________________________
#__________/VARIABLES GLOBALES
Root = Tk()
Fondo = PhotoImage(file = 'porsche_dash.png')
Icono = Root.iconbitmap('f1logo.ico')
Volante = PhotoImage(file="volante_0.png")
Dir_Izq_Off = PhotoImage(file="direccion_izquierda_default.png")        
Dir_Der_Off = PhotoImage(file="direccion_derecha_default.png")
Pedal_Clutch = PhotoImage(file="pedal.png")
Pedal_Break = PhotoImage(file="freno.png")
Pedal_Accelerator = PhotoImage(file="gas.png")
Palanca_Dir_Izq = PhotoImage(file="direccional.png")
Palanca_Dir_Der = PhotoImage(file="direccional_derecha.png")
Emergency = PhotoImage(file="emergencia_mini.png")
Headlights_Off = PhotoImage(file="off.png")
Headlights_On = PhotoImage(file="on.png")
Drive = PhotoImage(file="flecha_arriba.png")
Reverse = PhotoImage(file="flecha_abajo.png")
ZIGZAG = PhotoImage(file="zigzag_apagado.png")
INFINITE = PhotoImage(file="infinito_apagado.png")
CIRCLE = PhotoImage(file="circulo_apagado.png")
Winner = PhotoImage(file="Celebracion.png")
CUSTOM = PhotoImage(file='movimiento_especial_apagado.png')
Dir_Der_On = PhotoImage(file="direccion_derecha.png")
#           ____________________________
#__________/VENTANA PRINCIPAL
class Test_Drive_Ventana_Principal:
    def __init__(self, Root_TestDrive, Fondo_TestDrive, Icono_TestDrive, Volante_TestDrive,
                 Dir_Izq_Off_TestDrive, Dir_Der_Off_TestDrive, Pedal_Clutch_TestDrive,
                 Pedal_Break_TestDrive, Pedal_Accelerator_TestDrive, Palanca_Dir_Izq_TestDrive,
                 Palanca_Dir_Der_TestDrive, Emergency_TestDrive, Headlights_Off_TestDrive,
                 Headlights_On_TestDrive, Drive_TestDrive, Reverse_TestDrive, ZIGZAG_TestDrive,
                 INFINITE_TestDrive, CIRCLE_TestDrive, Winner_TestDrive, CUSTOM_TestDrive,
                 Dir_Der_On_TestDrive):
        #           ____________________________
        #__________/VARIABLES PRIVADAS
        self.Root_TestDrive = Root_TestDrive
        self.Fondo_TestDrive = Fondo_TestDrive
        self.Icono_TestDrive = Icono_TestDrive
        self.Volante_TestDrive = Volante_TestDrive
        self.Dir_Izq_Off_TestDrive = Dir_Izq_Off_TestDrive
        self.Dir_Der_Off_TestDrive = Dir_Der_Off_TestDrive
        self.Pedal_Clutch_TestDrive = Pedal_Clutch_TestDrive
        self.Pedal_Break_TestDrive = Pedal_Break_TestDrive
        self.Pedal_Accelerator_TestDrive = Pedal_Accelerator_TestDrive
        self.Palanca_Dir_Izq_TestDrive = Palanca_Dir_Izq_TestDrive
        self.Palanca_Dir_Der_TestDrive = Palanca_Dir_Der_TestDrive
        self.Emergency_TestDrive = Emergency_TestDrive
        self.Headlights_Off_TestDrive = Headlights_Off_TestDrive
        self.Headlights_On_TestDrive = Headlights_On_TestDrive
        self.Drive_TestDrive = Drive_TestDrive
        self.Reverse_TestDrive = Reverse_TestDrive
        self.ZIGZAG_TestDrive = ZIGZAG_TestDrive
        self.INFINITE_TestDrive = INFINITE_TestDrive
        self.CIRCLE_TestDrive = CIRCLE_TestDrive
        self.Winner_TestDrive = Winner_TestDrive
        self.CUSTOM_TestDrive = CUSTOM_TestDrive
        self.Dir_Der_On_TestDrive = Dir_Der_On_TestDrive
        #           ____________________________
        #__________/CONSTRUCTOR DE VENTANA
        Root_TestDrive.title("Formula 1 - ADJ")
        Root_TestDrive.config(bg="black",width=1485,height=800)
        Root_TestDrive.resizable(width=0,height=0)
        
        Label_Fondo_TestDrive = Label( Root_TestDrive, image = Fondo_TestDrive, bd =0).place(x=0,y=0)
        Label_Volante = Label( Root_TestDrive,image = Volante_TestDrive, bd =0).place(x=1202,y=0)
        Label_Dir_Izq_Off = Label( Root_TestDrive, image = Dir_Izq_Off_TestDrive, bd =0).place(x=1202,y=280)
        Label_Dir_Der_Off = Label( Root_TestDrive, image = Dir_Der_Off_TestDrive, bd =0).place(x=1342,y=280)
        

        Button_Pedal_Clutch_TestDrive = Button( Root_TestDrive, image = Pedal_Clutch_TestDrive, bd=0).place(x=245,y=440)
        Button_Pedal_Break_TestDrive = Button( Root_TestDrive, image = Pedal_Break_TestDrive, bd=0).place(x=400,y=440)
        Button_Pedal_Accelerator_TestDrive = Button( Root_TestDrive, image = Pedal_Accelerator_TestDrive, bd=0).place(x=514,y=440)
        Button_Palanca_Dir_Izq_TestDrive = Button( Root_TestDrive, image = Palanca_Dir_Izq_TestDrive, bd=0).place(x=275,y=298)
        Button_Palanca_Dir_Der_TestDrive = Button( Root_TestDrive, image = Palanca_Dir_Der_TestDrive, bd=0, command =lambda:self.thread_direccion_derecha(Thread)).place(x=515,y=298)
        Button_Emergency_TestDrive = Button( Root_TestDrive, image = Emergency_TestDrive, bd=0).place(x=420,y=370)
        Button_Headlights_On_TestDrive1 = Button( Root_TestDrive, image = Headlights_On_TestDrive, command = self.Frontales_Off, bd =0).place(x=1202,y=353)
        Button_Headlights_Off_TestDrive = Button( Root_TestDrive, image = Headlights_Off_TestDrive, command = self.Frontales_On, bd =0).place(x=1202,y=353)
        
        Button_Drive_TestDrive = Button( Root_TestDrive, image = Drive_TestDrive, bd=0).place(x=865,y=340)
        Button_Reverse_TestDrive = Button( Root_TestDrive, image = Reverse_TestDrive, bd=0).place(x=865,y=367)
        Button_Winner_TestDrive = Button( Root_TestDrive, image = Winner_TestDrive, bd=0).place(x=1358,y=353)
        Button_CIRCLE_TestDrive = Button( Root_TestDrive, image = CIRCLE_TestDrive, bd=0).place(x=683,y=230)
        Button_ZIGZAG_TestDrive = Button( Root_TestDrive, image = ZIGZAG_TestDrive, bd=0).place(x=703,y=175)
        Button_INFINITE_TestDrive = Button( Root_TestDrive, image = INFINITE_TestDrive, bd=0).place(x=673,y=175)
        Button_CUSTOM_TestDrive = Button( Root_TestDrive, image = CUSTOM_TestDrive, bd=0).place(x=683,y=265)
        
        
        Root_TestDrive.mainloop()
        
        #           ____________________________
        #__________/LUCES FRONTALES
    def Frontales_On(self):
        print("Headlights On")
        Button_Headlights_On_TestDrive = Button( self.Root_TestDrive, image = self.Headlights_On_TestDrive, bd =0, command = self.Frontales_Off).place(x=1202,y=353)
       
    def Frontales_Off(self):
        print("Headlights Off")
        Button_Headlights_Off_TestDrive = Button( self.Root_TestDrive, image = self.Headlights_Off_TestDrive, bd =0, command = self.Frontales_On).place(x=1202,y=353)
        #           ____________________________
        #__________/DIRECCIONALES
    def Dir_Der(self):
        x=0
        while(x<6):
            self.Label_Dir_Der_On = Label( self.Root_TestDrive, image = self.Dir_Der_On_TestDrive, bd =0).place(x=1342,y=280)
            time.sleep(0.5)
            self.Label_Dir_Der_Off = Label( self.Root_TestDrive, image = self.Dir_Der_Off_TestDrive, bd =0).place(x=1342,y=280)
            time.sleep(0.5)
            x+=1
    def thread_direccion_derecha(self,Thread):
        p = threading.Thread(target =self.Dir_Der)
        p.start()
        

        
#           ____________________________
#__________/INICIAR
Test_Drive_Ventana_Principal(Root, Fondo, Icono, Volante, Dir_Izq_Off, Dir_Der_Off,
                             Pedal_Clutch, Pedal_Break, Pedal_Accelerator, Palanca_Dir_Izq,
                             Palanca_Dir_Der, Emergency, Headlights_Off, Headlights_On, Drive,
                             Reverse, ZIGZAG, INFINITE, CIRCLE, Winner, CUSTOM, Dir_Der_On)






Root.mainloop()
