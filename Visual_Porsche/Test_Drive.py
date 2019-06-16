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
ZIGZAG_Off = PhotoImage(file="zigzag_apagado.png")
INFINITE_Off = PhotoImage(file="infinito_apagado.png")
CIRCLE_Off = PhotoImage(file="circulo_apagado.png")
Winner = PhotoImage(file="Celebracion.png")
CUSTOM_Off = PhotoImage(file='movimiento_especial_apagado.png')
Dir_Der_On = PhotoImage(file="direccion_derecha.png")
Dir_Izq_On = PhotoImage(file='direccion_izquierda.png')
CIRCLE_On = PhotoImage(file='circulo_encendido.png')
ZIGZAG_On = PhotoImage(file='zigzag.png')
INFINITE_On = PhotoImage(file='infinito_encendido.png')
CUSTOM1_On = PhotoImage(file="movimiento_especial1.png")
CUSTOM2_On = PhotoImage(file="movimiento_especial2.png")
CUSTOM3_On = PhotoImage(file="movimiento_especial3.png")
#           ____________________________
#__________/VENTANA PRINCIPAL
class Test_Drive_Ventana_Principal:
    def __init__(self, Root_TestDrive, Fondo_TestDrive, Icono_TestDrive, Volante_TestDrive,
                 Dir_Izq_Off_TestDrive, Dir_Der_Off_TestDrive, Pedal_Clutch_TestDrive,
                 Pedal_Break_TestDrive, Pedal_Accelerator_TestDrive, Palanca_Dir_Izq_TestDrive,
                 Palanca_Dir_Der_TestDrive, Emergency_TestDrive, Headlights_Off_TestDrive,
                 Headlights_On_TestDrive, Drive_TestDrive, Reverse_TestDrive, ZIGZAG_Off_TestDrive,
                 INFINITE_Off_TestDrive, CIRCLE_Off_TestDrive, Winner_TestDrive, CUSTOM_Off_TestDrive,
                 Dir_Der_On_TestDrive, Dir_Izq_On_TestDrive, CIRCLE_On_TestDrive, ZIGZAG_On_TestDrive,
                 INFINITE_On_TestDrive, CUSTOM1_On_TestDrive, CUSTOM2_On_TestDrive, CUSTOM3_On_TestDrive):
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
        self.ZIGZAG_Off_TestDrive = ZIGZAG_Off_TestDrive
        self.INFINITE_Off_TestDrive = INFINITE_Off_TestDrive
        self.CIRCLE_Off_TestDrive = CIRCLE_Off_TestDrive
        self.Winner_TestDrive = Winner_TestDrive
        self.CUSTOM_Off_TestDrive = CUSTOM_Off_TestDrive
        self.Dir_Der_On_TestDrive = Dir_Der_On_TestDrive
        self.Dir_Izq_On_TestDrive = Dir_Izq_On_TestDrive
        self.CIRCLE_On_TestDrive = CIRCLE_On_TestDrive
        self.ZIGZAG_On_TestDrive = ZIGZAG_On_TestDrive
        self.INFINITE_On_TestDrive = INFINITE_On_TestDrive
        self.CUSTOM1_On_TestDrive = CUSTOM1_On_TestDrive
        self.CUSTOM2_On_TestDrive = CUSTOM2_On_TestDrive
        self.CUSTOM3_On_TestDrive = CUSTOM3_On_TestDrive
        #           ____________________________
        #__________/CONSTRUCTOR DE VENTANA
        Root_TestDrive.title("Formula 1 - ADJ")
        Root_TestDrive.config(bg="gray",width=1480,height=800)
        Root_TestDrive.resizable(width=0,height=0)
        
        Label_Fondo_TestDrive = Label( Root_TestDrive, image = Fondo_TestDrive, bd =0).place(x=0,y=0)
        Label_Volante = Label( Root_TestDrive,image = Volante_TestDrive, bd =0).place(x=1200,y=0)
        Label_Dir_Izq_Off = Label( Root_TestDrive, image = Dir_Izq_Off_TestDrive, bd =0).place(x=1200,y=280)
        Label_Dir_Der_Off = Label( Root_TestDrive, image = Dir_Der_Off_TestDrive, bd =0).place(x=1340,y=280)
        

        Button_Pedal_Clutch_TestDrive = Button( Root_TestDrive, image = Pedal_Clutch_TestDrive, bd=0).place(x=245,y=440)
        Button_Pedal_Break_TestDrive = Button( Root_TestDrive, image = Pedal_Break_TestDrive, bd=0).place(x=400,y=440)
        Button_Pedal_Accelerator_TestDrive = Button( Root_TestDrive, image = Pedal_Accelerator_TestDrive, bd=0).place(x=514,y=440)
        Button_Palanca_Dir_Izq_TestDrive = Button( Root_TestDrive, image = Palanca_Dir_Izq_TestDrive, bd=0, command =lambda:self.thread_direccion_izquierda(Thread)).place(x=275,y=298)
        Button_Palanca_Dir_Der_TestDrive = Button( Root_TestDrive, image = Palanca_Dir_Der_TestDrive, bd=0, command =lambda:self.thread_direccion_derecha(Thread)).place(x=515,y=298)
        Button_Emergency_TestDrive = Button( Root_TestDrive, image = Emergency_TestDrive, bd=0, command = lambda:self.thread_parqueo(Thread)).place(x=420,y=370)
        Button_Headlights_On_TestDrive1 = Button( Root_TestDrive, image = Headlights_On_TestDrive, command = self.Frontales_Off, bd =0).place(x=1200,y=353)
        Button_Headlights_Off_TestDrive = Button( Root_TestDrive, image = Headlights_Off_TestDrive, command = self.Frontales_On, bd =0).place(x=1200,y=353)
        Button_Drive_TestDrive = Button( Root_TestDrive, image = Drive_TestDrive, bd=0).place(x=865,y=340)
        Button_Reverse_TestDrive = Button( Root_TestDrive, image = Reverse_TestDrive, bd=0).place(x=865,y=367)
        Button_Winner_TestDrive = Button( Root_TestDrive, image = Winner_TestDrive, bd=0).place(x=1350,y=353)
        Button_CIRCLE_Off_TestDrive = Button( Root_TestDrive, image = CIRCLE_Off_TestDrive, bd=0, command = lambda:self.thread_circulo(Thread)).place(x=680,y=230)
        Button_ZIGZAG_Off_TestDrive = Button( Root_TestDrive, image = ZIGZAG_Off_TestDrive, bd=0, command = lambda:self.thread_zigzag(Thread)).place(x=700,y=175)
        Button_INFINITE_Off_TestDrive = Button( Root_TestDrive, image = INFINITE_Off_TestDrive, bd=0, command = lambda:self.thread_infinito(Thread)).place(x=670,y=175)
        Button_CUSTOM_Off_TestDrive = Button( Root_TestDrive, image = CUSTOM_Off_TestDrive, bd=0, command = lambda:self.thread_especial(Thread)).place(x=680,y=265)
        
        
        Root_TestDrive.mainloop()
        
        #           ____________________________
        #__________/LUCES FRONTALES
    def Frontales_On(self):
        print("Headlights On")
        Button_Headlights_On_TestDrive = Button( self.Root_TestDrive, image = self.Headlights_On_TestDrive, bd =0, command = self.Frontales_Off).place(x=1200,y=353)
       
    def Frontales_Off(self):
        print("Headlights Off")
        Button_Headlights_Off_TestDrive = Button( self.Root_TestDrive, image = self.Headlights_Off_TestDrive, bd =0, command = self.Frontales_On).place(x=1200,y=353)
        #           ____________________________
        #__________/DIRECCIONALES
    def Dir_Der(self):
        x=0
        while(x<6):
            print("Dir Derecha On")
            Label_Dir_Der_On = Label( self.Root_TestDrive, image = self.Dir_Der_On_TestDrive, bd =0).place(x=1340,y=280)
            time.sleep(0.5)
            Label_Dir_Der_Off = Label( self.Root_TestDrive, image = self.Dir_Der_Off_TestDrive, bd =0).place(x=1340,y=280)
            time.sleep(0.5)
            x+=1
    def thread_direccion_derecha(self,Thread):
        p = threading.Thread(target =self.Dir_Der)
        p.start()
    def Dir_Izq(self):
        x=0
        while(x<6):
            print("Dir Izquierda On")
            Label_Dir_Izq_On = Label( self.Root_TestDrive, image = self.Dir_Izq_On_TestDrive, bd =0).place(x=1200,y=280)
            time.sleep(0.5)
            Label_Dir_Izq_Off = Label( self.Root_TestDrive, image = self.Dir_Izq_Off_TestDrive, bd =0).place(x=1200,y=280)
            time.sleep(0.5)
            x+=1
    def thread_direccion_izquierda(self,Thread):
        p = threading.Thread(target = self.Dir_Izq)
        p.start()
    def Emergency(self):
        x=0
        while(x<6):
            print("Emergency On")
            Label_Dir_Izq_On = Label( self.Root_TestDrive, image = self.Dir_Izq_On_TestDrive, bd =0).place(x=1200,y=280)
            Label_Dir_Der_On = Label( self.Root_TestDrive, image = self.Dir_Der_On_TestDrive, bd =0).place(x=1340,y=280) 
            time.sleep(0.5)
            Label_Dir_Izq_Off = Label( self.Root_TestDrive, image = self.Dir_Izq_Off_TestDrive, bd =0).place(x=1200,y=280)
            Label_Dir_Der_Off = Label( self.Root_TestDrive, image = self.Dir_Der_Off_TestDrive, bd =0).place(x=1340,y=280)
            time.sleep(0.5)
            x+=1        
    def thread_parqueo(self,Thread):
        p = threading.Thread(target = self.Emergency)
        p.start()
        #           ____________________________
        #__________/MOVIMIENTOS
    def circulo_cambio(self):
        x=0
        while(x<7):
            Button_CIRCLE_On_TestDrive = Button( self.Root_TestDrive, image = self.CIRCLE_On_TestDrive, bd=0).place(x=680,y=230)
            time.sleep(0.5)
            Button_CIRCLE_Off_TestDrive = Button( self.Root_TestDrive, image = self.CIRCLE_Off_TestDrive, bd=0, command = lambda:self.thread_circulo(Thread)).place(x=680,y=230)
            time.sleep(0.5)
            x+=1
    def thread_circulo(self,Thread):
        p = threading.Thread(target = self.circulo_cambio)
        p.start()
    def zigzag_cambio(self):
        x=0
        while(x<7):
            Button_ZIGZAG_On_TestDrive = Button( self.Root_TestDrive, image = self.ZIGZAG_On_TestDrive, bd=0).place(x=700,y=175)
            time.sleep(0.5)
            Button_ZIGZAG_Off_TestDrive = Button( self.Root_TestDrive, image = self.ZIGZAG_Off_TestDrive, bd=0, command = lambda:self.thread_zigzag(Thread)).place(x=700,y=175)
            time.sleep(0.5)
            x+=1
    def thread_zigzag(self,Thread):
        p = threading.Thread(target = self.zigzag_cambio)
        p.start()
    def infinito_cambio(self):
        x=0
        while(x<7):
            Button_INFINITE_On_TestDrive = Button( self.Root_TestDrive, image = self.INFINITE_On_TestDrive, bd=0).place(x=670,y=175)
            time.sleep(0.5)
            Button_INFINITE_Off_TestDrive = Button( self.Root_TestDrive, image = self.INFINITE_Off_TestDrive, bd=0, command = lambda:self.thread_infinito(Thread)).place(x=670,y=175)
            time.sleep(0.5)
            x+=1
    def thread_infinito(self,Thread):
        p = threading.Thread(target = self.infinito_cambio)
        p.start()
    def especial_cambio(self):
        global mov_especial
        x=0
        while(x<1):
            Button_CUSTOM_Off_TestDrive = Button( self.Root_TestDrive, image = self.CUSTOM_Off_TestDrive, bd=0, command = lambda:self.thread_especial(Thread)).place(x=680,y=265)
            time.sleep(0.3)
            i=0
            while(i<10):
                    Button_CUSTOM1_On_TestDrive = Button( self.Root_TestDrive, image = self.CUSTOM1_On_TestDrive, bd=0).place(x=680,y=265)
                    time.sleep(0.3)
                    Button_CUSTOM2_On_TestDrive = Button( self.Root_TestDrive, image = self.CUSTOM2_On_TestDrive, bd=0).place(x=680,y=265)
                    time.sleep(0.3)
                    Button_CUSTOM3_On_TestDrive = Button( self.Root_TestDrive, image = self.CUSTOM3_On_TestDrive, bd=0).place(x=680,y=265)
                    time.sleep(0.3)
                    i+=1
            Button_CUSTOM_Off_TestDrive = Button( self.Root_TestDrive, image = self.CUSTOM_Off_TestDrive, bd=0, command = lambda:self.thread_especial(Thread)).place(x=680,y=265)
            x+=1
    def thread_especial(self,Thread):
        p = threading.Thread(target = self.especial_cambio)
        p.start()
        
        
#           ____________________________
#__________/INICIAR
Test_Drive_Ventana_Principal(Root, Fondo, Icono, Volante, Dir_Izq_Off, Dir_Der_Off,
                             Pedal_Clutch, Pedal_Break, Pedal_Accelerator, Palanca_Dir_Izq,
                             Palanca_Dir_Der, Emergency, Headlights_Off, Headlights_On, Drive,
                             Reverse, ZIGZAG_Off, INFINITE_Off, CIRCLE_Off, Winner, CUSTOM_Off,
                             Dir_Der_On, Dir_Izq_On, CIRCLE_On, ZIGZAG_On , INFINITE_On,
                             CUSTOM1_On, CUSTOM2_On, CUSTOM3_On)


