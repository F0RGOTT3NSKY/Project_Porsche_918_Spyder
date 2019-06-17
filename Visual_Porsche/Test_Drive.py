#           _____________________________
#__________/BIBLIOTECAS
import tkinter
from tkinter import *
import time
import threading
from threading import *
import os
from Cliente_A_J import NodeMCU
#           ____________________________
#__________/VARIABLES GLOBALES
Root = Tk()
Fondo = PhotoImage(file = "porsche_dash.png")
Icono = Root.iconbitmap("f1logo.ico")
Dir_Izq_Off = PhotoImage(file = "direccion_izquierda_default.png")        
Dir_Der_Off = PhotoImage(file = "direccion_derecha_default.png")
Pedal_Clutch = PhotoImage(file = "pedal.png")
Pedal_Break = PhotoImage(file = "freno.png")
Pedal_Accelerator = PhotoImage(file = "gas.png")
Palanca_Dir_Izq = PhotoImage(file = "direccional.png")
Palanca_Dir_Der = PhotoImage(file = "direccional_derecha.png")
Emergency = PhotoImage(file = "emergencia_mini.png")
Headlights_Off = PhotoImage(file = "Off2.png")
Headlights_On = PhotoImage(file = "On2.png")
Drive = PhotoImage(file = "flecha_arriba.png")
Reverse = PhotoImage(file = "flecha_abajo.png")
ZIGZAG_Off = PhotoImage(file = "zigzag_apagado.png")
INFINITE_Off = PhotoImage(file = "infinito_apagado.png")
CIRCLE_Off = PhotoImage(file = "circulo_apagado.png")
Winner = PhotoImage(file = "Celebracion.png")
CUSTOM_Off = PhotoImage(file = "movimiento_especial_apagado.png")
Dir_Der_On = PhotoImage(file = "direccion_derecha.png")
Dir_Izq_On = PhotoImage(file = "direccion_izquierda.png")
CIRCLE_On = PhotoImage(file = "circulo_encendido.png")
ZIGZAG_On = PhotoImage(file = "zigzag.png")
INFINITE_On = PhotoImage(file = "infinito_encendido.png")
CUSTOM1_On = PhotoImage(file = "movimiento_especial1.png")
CUSTOM2_On = PhotoImage(file = "movimiento_especial2.png")
CUSTOM3_On = PhotoImage(file = "movimiento_especial3.png")
Girar_D = PhotoImage(file = "girar_derecha.png")
Girar_I = PhotoImage(file = "girar_izquierda.png")
Girar_0 = PhotoImage(file = "direccion_0.png")
Girar_D_On = PhotoImage(file = "girar_derecha_press.png")
Girar_I_On = PhotoImage(file = "girar_izquierda_press.png") 
Girar_0_On = PhotoImage(file = "direccion_0_press.png")
Volante = PhotoImage(file = "volante_0.png")
Volante_D_50 = PhotoImage(file = "volante_d_50.png")
Volante_D_90 = PhotoImage(file = "volante_d_90.png")
Volante_I_50 = PhotoImage(file = "volante_i_50.png")
Volante_I_90 = PhotoImage(file = "volante_i_90.png")
myCar = NodeMCU()
derecha = "dir:1;"
izquierda = "dir:-1;"
centro = "dir:0;"
direccional_der = "lr:;"  
direccional_izq = "ll:;"
emergency_On = "lp:;"
emergency_Off = "lo:;"
frontales_On = "lf:;"
frontales_Off = "lo:;"
circle = "CIRCLE:;"
zigzag = "ZIGZAG:;" 
infinite = "INFINITE:;"
custom = "CUSTOM:;"
moon = PhotoImage(file = 'luna.png')
sun = PhotoImage(file = 'sol.png')
bateria_llena = PhotoImage(file = 'bateria_llena.png')

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
                 INFINITE_On_TestDrive, CUSTOM1_On_TestDrive, CUSTOM2_On_TestDrive, CUSTOM3_On_TestDrive,
                 Girar_D_TestDrive, Girar_I_TestDrive, Girar_0_TestDrive, Girar_D_On_TestDrive,
                 Girar_I_On_TestDrive, Girar_0_On_TestDrive, Volante_D_50_TestDrive,
                 Volante_D_90_TestDrive, Volante_I_50_TestDrive, Volante_I_90_TestDrive, myCar_TestDrive, derecha_Testdrive,
                 izquierda_TestDrive, centro_TestDrive, direccional_der_TestDrive, direccional_izq_TestDrive, emergency_On_TestDrive,
                 emergency_Off_TestDrive, frontales_On_TestDrive, frontales_Off_TestDrive, circle_TestDrive,
                 zigzag_TestDrive, infinite_TestDrive, custom_TestDrive, moon_TestDrive, sun_TestDrive, bateria_llena_TestDrive):
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
        self.Girar_D_TestDrive = Girar_D_TestDrive
        self.Girar_I_TestDrive = Girar_I_TestDrive
        self.Girar_0_TestDrive = Girar_0_TestDrive
        self.Girar_D_On_TestDrive = Girar_D_On_TestDrive
        self.Girar_I_On_TestDrive = Girar_I_On_TestDrive
        self.Girar_0_On_TestDrive = Girar_0_On_TestDrive
        self.Volante_D_50_TestDrive = Volante_D_50_TestDrive
        self.Volante_D_90_TestDrive = Volante_D_90_TestDrive
        self.Volante_I_50_TestDrive = Volante_I_50_TestDrive
        self.Volante_I_90_TestDrive = Volante_I_90_TestDrive
        self.myCar_TestDrive = myCar_TestDrive
        self.derecha_Testdrive = derecha_Testdrive
        self.izquierda_TestDrive = izquierda_TestDrive
        self.centro_TestDrive = centro_TestDrive
        self.direccional_der_TestDrive = direccional_der_TestDrive
        self.direccional_izq_TestDrive = direccional_izq_TestDrive
        self.emergency_On_TestDrive = emergency_On_TestDrive
        self.emergency_Off_TestDrive = emergency_Off_TestDrive
        self.frontales_On_TestDrive = frontales_On_TestDrive
        self.frontales_Off_TestDrive = frontales_Off_TestDrive
        self.circle_TestDrive = circle_TestDrive
        self.zigzag_TestDrive = zigzag_TestDrive
        self.infinite_TestDrive = infinite_TestDrive
        self.custom_TestDrive = custom_TestDrive
        self.moon_TestDrive = moon_TestDrive
        self.sun_TestDrive = sun_TestDrive
        self.bateria_llena_TestDrive = bateria_llena_TestDrive
        myCar_TestDrive.start()
        
        #           ____________________________
        #__________/CONSTRUCTOR DE VENTANA
        Root_TestDrive.title("Formula 1 - ADJ")
        Root_TestDrive.config(bg="gray",width=1200,height=800)
        Root_TestDrive.resizable(width=0,height=0)
        
        Label_Fondo_TestDrive = Label( Root_TestDrive, image = Fondo_TestDrive, bd =0).place(x=0,y=0)
        Label_Volante = Label( Root_TestDrive, image = Volante_TestDrive, bd =0).place(x=744,y=174)
        Label_Escuderia = Label( Root_TestDrive, text = "                  PROPORSCHE2k19                  ", font = ("Comic Sans MS",6), relief = "sunken", bg = "black", fg = "white").place(x=743,y=248)
        Label_Dir_Izq_Off = Label( Root_TestDrive, image = Dir_Izq_Off_TestDrive, bd =0).place(x=348,y=195)
        Label_Dir_Der_Off = Label( Root_TestDrive, image = Dir_Der_Off_TestDrive, bd =0).place(x=505,y=195)
        Label_Bateria = Label( Root_TestDrive, image = bateria_llena_TestDrive, bd =0).place(x=812,y=205)
        Button_Moon = Button( Root_TestDrive, image = moon_TestDrive, bd = 0).place(x=810,y=174)
        

        Button_Pedal_Clutch_TestDrive = Button( Root_TestDrive, image = Pedal_Clutch_TestDrive, bd=0).place(x=245,y=440)
        Button_Pedal_Break_TestDrive = Button( Root_TestDrive, image = Pedal_Break_TestDrive, bd=0).place(x=400,y=450)
        Button_Pedal_Accelerator_TestDrive = Button( Root_TestDrive, image = Pedal_Accelerator_TestDrive, bd=0).place(x=514,y=440)
        
        Button_Palanca_Dir_Izq_TestDrive = Button( Root_TestDrive, image = Palanca_Dir_Izq_TestDrive, bd=0, command =lambda:self.thread_direccion_izquierda(Thread)).place(x=275,y=298)
        Button_Palanca_Dir_Der_TestDrive = Button( Root_TestDrive, image = Palanca_Dir_Der_TestDrive, bd=0, command =lambda:self.thread_direccion_derecha(Thread)).place(x=515,y=298)
        Button_Emergency_TestDrive = Button( Root_TestDrive, image = Emergency_TestDrive, bd=0, command = lambda:self.thread_parqueo(Thread,1)).place(x=152,y=238)
        
        Button_Headlights_On_TestDrive1 = Button( Root_TestDrive, image = Headlights_On_TestDrive, command = self.Frontales_Off, bd =0).place(x=148,y=193)
        Button_Headlights_Off_TestDrive = Button( Root_TestDrive, image = Headlights_Off_TestDrive, command = self.Frontales_On, bd =0).place(x=148,y=193)
        
        Button_Drive_TestDrive = Button( Root_TestDrive, image = Drive_TestDrive, bd=0).place(x=865,y=340)
        Button_Reverse_TestDrive = Button( Root_TestDrive, image = Reverse_TestDrive, bd=0).place(x=865,y=367)
        Button_Winner_TestDrive = Button( Root_TestDrive, image = Winner_TestDrive, bd=0).place(x=833,y=174)
        
        Button_CIRCLE_Off_TestDrive = Button( Root_TestDrive, image = CIRCLE_Off_TestDrive, bd=0, command = lambda:self.seleccion_moviento(0)).place(x=679,y=218)
        Button_ZIGZAG_Off_TestDrive = Button( Root_TestDrive, image = ZIGZAG_Off_TestDrive, bd=0, command = lambda:self.seleccion_moviento(1)).place(x=698,y=170)
        Button_INFINITE_Off_TestDrive = Button( Root_TestDrive, image = INFINITE_Off_TestDrive, bd=0, command = lambda:self.seleccion_moviento(2)).place(x=672,y=170)
        Button_CUSTOM_Off_TestDrive = Button( Root_TestDrive, image = CUSTOM_Off_TestDrive, bd=0, command = lambda:self.seleccion_moviento(3)).place(x=679,y=256)
        
        Button_Girar_D = Button( Root_TestDrive, bd=0, image = Girar_D_TestDrive, command = lambda:self.thread_girar_derecha(Thread)).place(x=515,y=220)
        Button_Girar_I = Button( Root_TestDrive, bd=0, image = Girar_I_TestDrive, command = lambda:self.thread_girar_izquierda(Thread)).place(x=312,y=222)
        Button_Girar_0 = Button( Root_TestDrive, bd=0, image = Girar_0_TestDrive, command = lambda:self.thread_posicion_0(Thread)).place(x=416,y=360)
        
        Root_TestDrive.mainloop()
        #           ____________________________
        #__________/SEND NUDES

    def send (self,comando):
        x=0
        while(x<1):
            mns = str(comando)
            myCar.send(mns)
            print ("Enviando mensaje: ",comando)
            x+=1
        #           ____________________________
        #__________/SENSOR DE LUZ
    def oscuro(self):
        x=0
        while(x<1):
            Label_Moon = Label( self.Root_TestDrive, image = self.moon_TestDrive, bd = 0, bg = "black").place(x=867,y=176)
            time.sleep(0.5)
            Label_Sun = Label( self.Root_TestDrive, image = self.sun_TestDrive, bd = 0).place(x=867,y=176)
            x+=1
    def thread_luz_oscuridad(self,Thread):
        p = threading.Thread(target = self.oscuro)
        p.start()
    def sol(self):
        x=0
        while(x<1):
            Label_Sun = Label( self.Root_TestDrive, image = self.sun_TestDrive, bd = 0).place(x=867,y=176)
            time.sleep(0.5)
            Label_Moon = Label( self.Root_TestDrive, image = self.moon_TestDrive, bd = 0, bg = "black").place(x=867,y=176)
            x+=1
    def thread_sol(self,Thread):
        p = threading.Thread(target = self.sol)
        p.start()
    #def thread_luz(self,Thread):
        
        #           ____________________________
        #__________/DIRECCION
                  
    def girar_derecha(self):
        x=0
        while(x<1):
            Button_Girar_D = Button( self.Root_TestDrive, bd=0, image = self.Girar_D_On_TestDrive).place(x=515,y=220)
            Label_Volante = Label( self.Root_TestDrive, image = self.Volante_TestDrive, bd =0).place(x=744,y=174)
            time.sleep(0.3)
            Label_Volante = Label( self.Root_TestDrive, image = self.Volante_D_50_TestDrive , bd =0).place(x=744,y=174)
            time.sleep(0.3)
            Button_Girar_D = Button( self.Root_TestDrive, bd=0, image = self.Girar_D_TestDrive, command = lambda:self.thread_girar_derecha(Thread)).place(x=515,y=220)
            Label_Volante = Label( self.Root_TestDrive, image = self.Volante_D_90_TestDrive, bd =0).place(x=744,y=174)
            
            x+=1
    def thread_girar_derecha(self,Thread):
        p = threading.Thread(target = self.girar_derecha)
        p.start()
        comando = self.derecha_Testdrive 
        t = threading.Thread(target = self.send(comando))
        t.start()
    def girar_izquierda(self):
        x=0
        while(x<1):
            Button_Girar_I = Button( self.Root_TestDrive, bd=0, image = self.Girar_I_On_TestDrive).place(x=312,y=222)
            Label_Volante = Label( self.Root_TestDrive, image = self.Volante_TestDrive, bd =0).place(x=744,y=174)
            time.sleep(0.3)
            Label_Volante = Label( self.Root_TestDrive, image = self.Volante_I_50_TestDrive, bd =0).place(x=744,y=174)
            time.sleep(0.3)
            Button_Girar_I = Button( self.Root_TestDrive, bd=0, image = self.Girar_I_TestDrive, command = lambda:self.thread_girar_izquierda(Thread)).place(x=312,y=222)
            Label_Volante = Label( self.Root_TestDrive, image = self.Volante_I_90_TestDrive, bd =0).place(x=744,y=174)
            x+=1      
    def thread_girar_izquierda(self,Thread):
        p = threading.Thread(target = self.girar_izquierda)
        p.start()
        comando = self.izquierda_TestDrive
        t = threading.Thread(target = self.send(comando))
        t.start()      
    def girar_0(self):
        x=0
        while(x<1):
            Label_Volante = Label( self.Root_TestDrive, image = self.Volante_TestDrive, bd =0).place(x=744,y=174)
            Button_Girar_0 = Button( self.Root_TestDrive, bd=0, image = self.Girar_0_On_TestDrive, command = lambda:self.thread_posicion_0(Thread)).place(x=416,y=360)
            time.sleep(1)
            Button_Girar_0 = Button( self.Root_TestDrive, bd=0, image = self.Girar_0_TestDrive, command = lambda:self.thread_posicion_0(Thread)).place(x=416,y=360)
            x+=1
    def thread_posicion_0(self,Thread):
        p = threading.Thread(target = self.girar_0)
        p.start()
        comando = self.centro_TestDrive
        t = threading.Thread(target = self.send(comando))
        t.start()
        #           ____________________________
        #__________/LUCES FRONTALES
    def Frontales_On(self):
        print("Headlights On")
        Button_Headlights_On_TestDrive = Button( self.Root_TestDrive, image = self.Headlights_On_TestDrive, bd =0, command = self.Frontales_Off).place(x=148,y=193)
        comando = self.frontales_On_TestDrive 
        t = threading.Thread(target = self.send(comando))
        t.start()
       
    def Frontales_Off(self):
        print("Headlights Off")
        Button_Headlights_Off_TestDrive = Button( self.Root_TestDrive, image = self.Headlights_Off_TestDrive, bd =0, command = self.Frontales_On).place(x=148,y=193)
        comando = self.frontales_Off_TestDrive 
        t = threading.Thread(target = self.send(comando))
        t.start()
        #           ____________________________
        #__________/DIRECCIONALES
    def Dir_Der(self):
        x=0
        while(x<8):
            print("Dir Derecha On")
            Label_Dir_Der_On = Label( self.Root_TestDrive, image = self.Dir_Der_On_TestDrive, bd =0).place(x=505,y=195)
            time.sleep(0.5)
            Label_Dir_Der_Off = Label( self.Root_TestDrive, image = self.Dir_Der_Off_TestDrive, bd =0).place(x=505,y=195)
            time.sleep(0.5)
            x+=1
    def thread_direccion_derecha(self,Thread):
        p = threading.Thread(target =self.Dir_Der)
        p.start()
        comando = self.direccional_der_TestDrive 
        t = threading.Thread(target = self.send(comando))
        t.start()
    def Dir_Izq(self):
        x=0
        while(x<8):
            print("Dir Izquierda On")
            Label_Dir_Izq_On = Label( self.Root_TestDrive, image = self.Dir_Izq_On_TestDrive, bd =0).place(x=348,y=195)
            time.sleep(0.5)
            Label_Dir_Izq_Off = Label( self.Root_TestDrive, image = self.Dir_Izq_Off_TestDrive, bd =0).place(x=348,y=195)
            time.sleep(0.5)
            x+=1
    def thread_direccion_izquierda(self,Thread):
        p = threading.Thread(target = self.Dir_Izq)
        p.start()
        comando = self.direccional_izq_TestDrive 
        t = threading.Thread(target = self.send(comando))
        t.start()
    def Emergency(self):
        Button_Emergency_TestDrive = Button( self.Root_TestDrive, image = self.Emergency_TestDrive, bd=0, command = lambda:self.thread_parqueo(Thread,0)).place(x=152,y=238)
        x=0
        while(x<8):
            print("Emergency On")
            Label_Dir_Izq_On = Label( self.Root_TestDrive, image = self.Dir_Izq_On_TestDrive, bd =0).place(x=348,y=195)
            Label_Dir_Der_On = Label( self.Root_TestDrive, image = self.Dir_Der_On_TestDrive, bd =0).place(x=505,y=195) 
            time.sleep(0.5)
            Label_Dir_Izq_Off = Label( self.Root_TestDrive, image = self.Dir_Izq_Off_TestDrive, bd =0).place(x=348,y=195)
            Label_Dir_Der_Off = Label( self.Root_TestDrive, image = self.Dir_Der_Off_TestDrive, bd =0).place(x=505,y=195)
            time.sleep(0.5)
            x+=1 
    def Emergency_Off(self):
        Button_Emergency_TestDrive = Button( self.Root_TestDrive, image = self.Emergency_TestDrive, bd=0, command = lambda:self.thread_parqueo(Thread,1)).place(x=152,y=238)
        print("Emergency Off")
        Label_Dir_Izq_Off = Label( self.Root_TestDrive, image = self.Dir_Izq_Off_TestDrive, bd =0).place(x=348,y=195)
        Label_Dir_Der_Off = Label( self.Root_TestDrive, image = self.Dir_Der_Off_TestDrive, bd =0).place(x=505,y=195)
    def thread_parqueo(self,Thread,x):
            if(x==0):
                p = threading.Thread(target = self.Emergency_Off)
                p.start()
                comando = self.emergency_Off_TestDrive 
                t = threading.Thread(target = self.send(comando))
                t.start()
            else:
                p = threading.Thread(target = self.Emergency)
                p.start()
                comando = self.emergency_On_TestDrive 
                t = threading.Thread(target = self.send(comando))
                t.start()
            
        
        #           ____________________________
        #__________/MOVIMIENTOS
    def seleccion_moviento(self,x):
        if(x==0):
            p = threading.Thread(target = self.circulo_cambio)
            p.start()
            comando = self.circle_TestDrive
            t = threading.Thread(target = self.send(comando))
            t.start()
            
        elif(x==1):
            p = threading.Thread(target = self.zigzag_cambio)
            p.start()
            comando = self.zigzag_TestDrive 
            t = threading.Thread(target = self.send(comando))
            t.start()
        elif(x==2):
            p = threading.Thread(target = self.infinito_cambio)
            p.start()
            comando = self.infinite_TestDrive 
            t = threading.Thread(target = self.send(comando))
            t.start()
        elif(x==3):
            p = threading.Thread(target = self.especial_cambio)
            p.start()
            comando = self.custom_TestDrive
            t = threading.Thread(target = self.send(comando))
            t.start()
        else:
            print("Error en Movimiento")
    def circulo_cambio(self):
        x=0
        while(x<2):
            Button_CIRCLE_On_TestDrive = Button( self.Root_TestDrive, image = self.CIRCLE_On_TestDrive, bd=0).place(x=679,y=218)
            time.sleep(0.5)
            Button_CIRCLE_Off_TestDrive = Button( self.Root_TestDrive, image = self.CIRCLE_Off_TestDrive, bd=0, command = lambda:self.seleccion_moviento(0)).place(x=679,y=218)
            time.sleep(0.5)
            x+=1    
    def zigzag_cambio(self):
        x=0
        while(x<5):
            Button_ZIGZAG_On_TestDrive = Button( self.Root_TestDrive, image = self.ZIGZAG_On_TestDrive, bd=0).place(x=698,y=170)
            time.sleep(0.5)
            Button_ZIGZAG_Off_TestDrive = Button( self.Root_TestDrive, image = self.ZIGZAG_Off_TestDrive, bd=0, command = lambda:self.seleccion_moviento(1)).place(x=698,y=170)
            time.sleep(0.5)
            x+=1
    def infinito_cambio(self):
        x=0
        while(x<4):
            Button_INFINITE_On_TestDrive = Button( self.Root_TestDrive, image = self.INFINITE_On_TestDrive, bd=0).place(x=672,y=170)
            time.sleep(0.5)
            Button_INFINITE_Off_TestDrive = Button( self.Root_TestDrive, image = self.INFINITE_Off_TestDrive, bd=0, command = lambda:self.seleccion_moviento(2)).place(x=672,y=170)
            time.sleep(0.5)
            x+=1
    def especial_cambio(self):
        x=0
        while(x<1):
            Button_CUSTOM_Off_TestDrive = Button( self.Root_TestDrive, image = self.CUSTOM_Off_TestDrive, bd=0, command = lambda:self.seleccion_moviento(3)).place(x=679,y=256)
            time.sleep(0.3)
            i=0
            while(i<3):
                    Button_CUSTOM1_On_TestDrive = Button( self.Root_TestDrive, image = self.CUSTOM1_On_TestDrive, bd=0).place(x=679,y=256)
                    time.sleep(0.3)
                    Button_CUSTOM2_On_TestDrive = Button( self.Root_TestDrive, image = self.CUSTOM2_On_TestDrive, bd=0).place(x=679,y=256)
                    time.sleep(0.3)
                    Button_CUSTOM3_On_TestDrive = Button( self.Root_TestDrive, image = self.CUSTOM3_On_TestDrive, bd=0).place(x=679,y=256)
                    time.sleep(0.3)
                    i+=1
            Button_CUSTOM_Off_TestDrive = Button( self.Root_TestDrive, image = self.CUSTOM_Off_TestDrive, bd=0, command = lambda:self.seleccion_moviento(3)).place(x=679,y=256)
            x+=1
        
#           ____________________________
#__________/INICIAR
Test_Drive_Ventana_Principal(Root, Fondo, Icono, Volante, Dir_Izq_Off, Dir_Der_Off,
                             Pedal_Clutch, Pedal_Break, Pedal_Accelerator, Palanca_Dir_Izq,
                             Palanca_Dir_Der, Emergency, Headlights_Off, Headlights_On, Drive,
                             Reverse, ZIGZAG_Off, INFINITE_Off, CIRCLE_Off, Winner, CUSTOM_Off,
                             Dir_Der_On, Dir_Izq_On, CIRCLE_On, ZIGZAG_On , INFINITE_On,
                             CUSTOM1_On, CUSTOM2_On, CUSTOM3_On, Girar_D, Girar_I, Girar_0, Girar_D_On,
                             Girar_I_On, Girar_0_On, Volante_D_50, Volante_D_90, Volante_I_50, Volante_I_90,
                             myCar, derecha, izquierda, centro, direccional_der, direccional_izq, emergency_On,
                             emergency_Off, frontales_On, frontales_Off, circle, zigzag, infinite, custom, moon, sun, bateria_llena)



