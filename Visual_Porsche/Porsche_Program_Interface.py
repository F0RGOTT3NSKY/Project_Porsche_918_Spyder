#           _____________________________
#__________/BIBLIOTECAS
from tkinter import *
#           _____________________________
#__________/BIBLIOTECAS
import tkinter
from tkinter import *
import time
import threading
from threading import *
import os
from Cliente_A_J import NodeMCU


#           _____________________________
#__________/VENTANA PRINCIPAL
class Main_Interface:
    def __init__(self):
        self.Root_Main = None
    
    def Main(self):
        #           _____________________________
        #__________/VARIABLES PRIVADAS
        self.Root_Main = Tk()
        self.fondo_Main = PhotoImage(file='spyder.png')
        self.icono_Main = self.Root_Main.iconbitmap('f1logo.ico')
        self.patrocinador_imagen_Main = PhotoImage(file='SHELL_mini.gif')
        self.patrocinador2_imagen_Main = PhotoImage(file='firelli_mini.gif')
        self.patrocinador3_imagen_Main = PhotoImage(file='marlboro_mini.gif')
        self.f1_Main = PhotoImage(file='f1mini.gif')
        self.imagen_Main = PhotoImage(file='about.png')
        self.devolver_Main = PhotoImage(file='girar_izquierda_press.png') 
        self.Fondo_TestDrive = PhotoImage(file = "porsche_dash.png")
        self.Icono_TestDrive = self.Root_Main.iconbitmap("f1logo.ico")
        self.Dir_Izq_Off_TestDrive = PhotoImage(file = "direccion_izquierda_default.png") 
        self.Dir_Der_Off_TestDrive = PhotoImage(file = "direccion_derecha_default.png") 
        self.Pedal_Clutch_TestDrive = PhotoImage(file = "pedal.png")
        self.Pedal_Break_TestDrive = PhotoImage(file = "freno.png")
        self.Pedal_Accelerator_TestDrive = PhotoImage(file = "gas.png")
        self.Palanca_Dir_Izq_TestDrive = PhotoImage(file = "direccional.png")
        self.Palanca_Dir_Der_TestDrive = PhotoImage(file = "direccional_derecha.png")
        self.Emergency_TestDrive = PhotoImage(file = "emergencia_mini.png")
        self.Headlights_Off_TestDrive = PhotoImage(file = "Off2.png") 
        self.Headlights_On_TestDrive = PhotoImage(file = "On2.png")
        self.Drive_TestDrive = PhotoImage(file = "flecha_arriba.png") 
        self.Reverse_TestDrive = PhotoImage(file = "flecha_abajo.png")
        self.ZIGZAG_Off_TestDrive = PhotoImage(file = "zigzag_apagado.png")
        self.INFINITE_Off_TestDrive = PhotoImage(file = "infinito_apagado.png")
        self.CIRCLE_Off_TestDrive = PhotoImage(file = "circulo_apagado.png")
        self.Winner_TestDrive = PhotoImage(file = "Celebracion.png")
        self.CUSTOM_Off_TestDrive = PhotoImage(file = "movimiento_especial_apagado.png")
        self.Dir_Der_On_TestDrive = PhotoImage(file = "direccion_derecha.png")
        self.Dir_Izq_On_TestDrive = PhotoImage(file = "direccion_izquierda.png")
        self.CIRCLE_On_TestDrive = PhotoImage(file = "circulo_encendido.png")
        self.ZIGZAG_On_TestDrive = PhotoImage(file = "zigzag.png")
        self.INFINITE_On_TestDrive = PhotoImage(file = "infinito_encendido.png")
        self.CUSTOM1_On_TestDrive = PhotoImage(file = "movimiento_especial1.png")
        self.CUSTOM2_On_TestDrive = PhotoImage(file = "movimiento_especial2.png")
        self.CUSTOM3_On_TestDrive = PhotoImage(file = "movimiento_especial3.png")
        self.Girar_D_TestDrive = PhotoImage(file = "girar_derecha.png")
        self.Girar_I_TestDrive = PhotoImage(file = "girar_izquierda.png")
        self.Girar_0_TestDrive = PhotoImage(file = "direccion_0.png")
        self.Girar_D_On_TestDrive = PhotoImage(file = "girar_derecha_press.png")
        self.Girar_I_On_TestDrive = PhotoImage(file = "girar_izquierda_press.png") 
        self.Girar_0_On_TestDrive = PhotoImage(file = "direccion_0_press.png")
        self.Volante_TestDrive = PhotoImage(file = "volante_0.png")
        self.Volante_D_50_TestDrive = PhotoImage(file = "volante_d_50.png")
        self.Volante_D_90_TestDrive = PhotoImage(file = "volante_d_90.png")
        self.Volante_I_50_TestDrive = PhotoImage(file = "volante_i_50.png")
        self.Volante_I_90_TestDrive = PhotoImage(file = "volante_i_90.png")
        self.myCar_TestDrive = NodeMCU()
        self.derecha_Testdrive = "dir:1;"
        self.izquierda_TestDrive = "dir:-1;"
        self.centro_TestDrive = "dir:0;"
        self.direccional_der_TestDrive = "lr:;"  
        self.direccional_izq_TestDrive = "ll:;"
        self.emergency_On_TestDrive = "lp:;"
        self.emergency_Off_TestDrive = "lo:;"
        self.frontales_On_TestDrive = "lf:;"
        self.frontales_Off_TestDrive = "lo:;"
        self.circle_TestDrive = "CIRCLE:;"
        self.zigzag_TestDrive = "ZIGZAG:;" 
        self.infinite_TestDrive = "INFINITE:;"
        self.custom_TestDrive = "CUSTOM:;"
        self.moon_TestDrive = PhotoImage(file = 'luna.png')
        self.sun_TestDrive = PhotoImage(file = 'sol.png')
        self.bateria_llena_TestDrive = PhotoImage(file = 'bateria_llena.png')
        self.velocidad_TestDrive = "Ninguno"
        self.pwm_controller_TestDrive = "Ninguno"
        self.Pedal_TestDrive = "Ninguno"
        self.Fondo_Blanco_Main = PhotoImage(file = "fondo_blanco.png")
        self.myCar_TestDrive.start()
        #           _____________________________
        #__________/CONSTRUCTOR DE VENTANA
        self.Root_Main.title("Formula 1 - ADJ")
        self.Root_Main.config(bg="#8B0000",width="1200", height="800")
        label_de_imagen=Label(self.Root_Main,image=self.fondo_Main).place(x=0,y=0)
        self.Root_Main.resizable(height=0,width=0)
        logo=Label(self.Root_Main,image=self.f1_Main).place(x=10,y=10)
        
        escuderia=Label(self.Root_Main,text="Nombre de Escuderia:",font='helvetica 12',justify=CENTER,width="17",height="3",bg="black",fg="white").place(x=140,y=10)
        Ubicacion=Label(self.Root_Main,text="Ubicacion:",font='helvetica 12',width="17",height="3",bg="black",fg="white").place(x=140,y=75)
        Patrocinadores=Label(self.Root_Main,text="Patrocinadores:",font='helvetica 12',width="17",height="3",bg="black",fg="white").place(x=140,y=140)
        escuderia_nombre=Label(self.Root_Main,text="PROPORSCHE2k19",font='helvetica 12',width="17",height="3",bg="#8B0000",fg="white",relief="groove").place(x=310,y=10)
        pais_ubicacion=Label(self.Root_Main,text="COSTA RICA",font='helvetica 12',width="17",height="3",bg="#8B0000",fg="white",relief="groove").place(x=310,y=75)
        patrocinador1=Label(self.Root_Main,image=self.patrocinador_imagen_Main,relief="solid").place(x=310,y=140)
        patrocinador2=Label(self.Root_Main,image=self.patrocinador2_imagen_Main,relief="solid").place(x=440,y=140)
        patrocinador3=Label(self.Root_Main,image=self.patrocinador3_imagen_Main,relief="solid").place(x=650,y=140)
    
        minim = Button(self.Root_Main, text="MINIMIZAR", command=self.Root_Main.iconify,justify=CENTER,bg="#454545",fg="white",relief="raised",bd=15).place(x=1030,y=10)
        salida = Button(self.Root_Main, text="SALIR", command=self.Root_Main.destroy,justify=CENTER,bg="#454545",fg="white",relief="raised",bd=15).place(x=950,y=10)

        tabla = Button(self.Root_Main, text="TABLA DE POSICIONES",font=("Comic Sans MS",10),width=18, justify=CENTER,bg="#800000",fg="white",relief="raised",bd=15,command = self.Ventana_Tabla).place(x=950,y=100)
        historial = Button(self.Root_Main, text="HISTORIAL DE AUTOS",font=("Comic Sans MS",10),width=18 ,justify=CENTER,bg="#454545",fg="white",relief="raised",bd=15,command = self.ventana_principal).place(x=950,y=160)
        drive = Button(self.Root_Main, text="TEST DRIVE",width=18,font=("Comic Sans MS",10),justify=CENTER,bg="#800000",fg="white",relief="raised",bd=15,command = self.abrir).place(x=950,y=220)

        tabla = Button(self.Root_Main, text="TABLA DE POSICIONES",font=("Comic Sans MS",10),width=18, justify=CENTER,bg="#800000",fg="white",relief="raised",bd=15).place(x=950,y=100)
        historial = Button(self.Root_Main, text="HISTORIAL DE AUTOS",font=("Comic Sans MS",10),width=18 ,justify=CENTER,bg="#454545",fg="white",relief="raised",bd=15).place(x=950,y=160)
        drive = Button(self.Root_Main, text="TEST DRIVE",width=18,font=("Comic Sans MS",10),justify=CENTER,bg="#800000",fg="white",relief="raised",bd=15,command = self.Ventana_TestDrive).place(x=950,y=220)

        editar = Button(self.Root_Main, text="EDITAR", width=18,font=("Comic Sans MS",10),justify=CENTER,bg="#454545",fg="white",relief="raised",bd=15).place(x=950,y=280)
        about = Button(self.Root_Main, text="MÁS...",font=("Comic Sans MS",10),width=18,justify=CENTER,bg="#800000",fg="white",relief="raised",bd=15,command = self.Ventana_About).place(x=950,y=340)

        self.Root_Main.mainloop()

        
    def abrir(self):
        self.Root_Main.destroy()
        self.ventana_principal()
    
    def ventana_principal(self):
        self.Root_Main.title("historial de autos")
        icono=self.Root_Main.iconbitmap('f1logo.ico')
        self.Root_Main.resizable(width=False,height=False)
        self.Root_Main.config(width=1200,height=800,bg="gray")
        fondo=PhotoImage(file='fondo_para_historial.png')
        fondo_porsche=Label(self.Root_Main,image=fondo).place(x=0,y=0)

        devolver=PhotoImage(file='girar_izquierda_press.png')
        boton_de_devolver=Button(self.Root_Main,image=devolver,relief="raised").place(x=1100,y=700)

        ### BOTONES DE VEHICULOS ###

        vehiculo1=Button(self.Root_Main,fg="white",text="Mercedes-AMG F1 M10",bg="#f22424",relief="raised",bd=10,command=lambda: self.revisar(1)).place(x=70,y=10)

        vehiculo2=Button(self.Root_Main,fg="white",text="Ferrari 064",bg="#f22424",relief="raised",bd=10,command=lambda: self.revisar(2)).place(x=70,y=100)

        vehiculo3=Button(self.Root_Main,fg="white",text="Honda RA619H9",bg="#f22424",relief="raised",bd=10).place(x=70,y=190)

        vehiculo4=Button(self.Root_Main,fg="white",text="Renault E-Tech 19",bg="#f22424",bd=10,relief="raised").place(x=70,y=280)

        vehiculo5=Button(self.Root_Main,fg="white",text="Ferrari 06413",bg="#f22424",bd=10,relief="raised").place(x=70,y=370)

        vehiculo6=Button(self.Root_Main,fg="white",text="Renault E-Tech 1916",bg="#f22424",bd=10,relief="raised").place(x=900,y=10)

        vehiculo7=Button(self.Root_Main,fg="white",text="BWT Mercedes-AMG F1",bg="#f22424",bd=10,relief="raised").place(x=900,y=100)

        vehiculo8=Button(self.Root_Main,fg="white",text="Ferrari 06426",bg="#f22424",bd=10,relief="raised").place(x=900,y=190)

        vehiculo9=Button(self.Root_Main,fg="white",text="Honda RA619H28",bg="#f22424",bd=10,relief="raised").place(x=900,y=280)

        vehiculo10=Button(self.Root_Main,fg="white",text="Mercedes-AMG F1 M10 EQ Power+31",bg="#f22424",bd=10,relief="raised").place(x=900,y=370)
        self.Root_Main.mainloop()
    def ventana1(self):
        ## VENTANA 1 ## 
        self.ventana1=Toplevel()
        self.ventana1.config(width=500,height=500)
        pistaIma=PhotoImage(file='pista.png')
        self.ventana1.resizable(width=False,height=False)
        pista=Label(self.ventana1,image=pistaIma).place(x=0,y=0)
        icono=self.ventana1.iconbitmap('f1logo.ico')
        vehiculo1=PhotoImage(file='auto1.png')
        carro1=Label(self.ventana1,image=vehiculo1)
        carro1.place(x=0,y=0)
        ### ESPECIFICACIONES ##
        nombre=Label(self.ventana1,text='nombre:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=140)
        pais=Label(self.ventana1,text='Pais:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=170)
        modelo=Label(self.ventana1,text='Modelo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=200)
        estado=Label(self.ventana1,text='Estado:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=230)
        consumo=Label(self.ventana1,text='Consumo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=260)
        sensores=Label(self.ventana1,text='Sensores:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=290)
        peso=Label(self.ventana1,text='Peso:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=320)
        baterias=Label(self.ventana1,text='baterias:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=350)
        tension=Label(self.ventana1,text='tension:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=380)
        eficiencia=Label(self.ventana1,text='Eficiencia:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=410)
        temporada=Label(self.ventana1,text='Temporada:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=440)
        ppB=Label(self.ventana1,text='PPB:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=470)
        
        ### RESPUESTA  ###
        nombre=Label(self.ventana1,text='Mercedes-AMG',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=140)
        pais=Label(self.ventana1,text='FINLANDIA',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=170)
        modelo=Label(self.ventana1,text='2019',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=200)
        estado=Label(self.ventana1,text='Disponible',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=230)
        consumo=Label(self.ventana1,text='1,29V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=260)
        sensores=Label(self.ventana1,text='Luz',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=290)
        peso=Label(self.ventana1,text='744kg',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=320)
        baterias=Label(self.ventana1,text='1',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=350)
        tension=Label(self.ventana1,text='0,29V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=380)
        eficiencia=Label(self.ventana1,text='8',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=410)
        temporada=Label(self.ventana1,text='2016',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=440)
        ppB=Label(self.ventana1,text='5',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=470)
        
        self.ventana1.mainloop()
        
    def ventana2(self):
        self.ventana2=Toplevel()
        self.ventana2.config(width=500,height=500,bg="black")
        icono=self.ventana2.iconbitmap('f1logo.ico')
        self.ventana2.resizable(width=False,height=False)
        pistaIma=PhotoImage(file='pista.png')
        pista=Label(self.ventana2,image=pistaIma).place(x=0,y=0)
        vehiculo2=PhotoImage(file='auto2.png')
        carro2=Label(self.ventana2,image=vehiculo2)
        carro2.place(x=0,y=0)
        nombre=Label(self.ventana2,text='nombre:',bd=4,bg="black",fg="white").place(x=10,y=140)
        pais=Label(self.ventana2,text='Pais:',bd=4,bg="black",fg="white").place(x=10,y=170)
        modelo=Label(self.ventana2,text='Modelo:',bd=4,bg="black",fg="white").place(x=10,y=200)
        estado=Label(self.ventana2,text='Estado:',bd=4,bg="black",fg="white").place(x=10,y=230)
        consumo=Label(self.ventana2,text='Consumo:',bd=4,bg="black",fg="white").place(x=10,y=260)
        sensores=Label(self.ventana2,text='Sensores:',bd=4,bg="black",fg="white").place(x=10,y=290)
        peso=Label(self.ventana2,text='Peso:',bd=4,bg="black",fg="white").place(x=10,y=320)
        baterias=Label(self.ventana2,text='baterias:',bd=4,bg="black",fg="white").place(x=10,y=350)
        tension=Label(self.ventana2,text='tension:',bd=4,bg="black",fg="white").place(x=10,y=380)
        eficiencia=Label(self.ventana2,text='Eficiencia:',bd=4,bg="black",fg="white").place(x=10,y=410)
        temporada=Label(self.ventana2,text='Temporada:',bd=4,bg="black",fg="white").place(x=10,y=440)
        ppB=Label(self.ventana2,text='PPB:',bd=4,bg="black",fg="white").place(x=10,y=470)
        ### RESPUESTA  ###
        nombre=Label(self.ventana2,text='FERRARI 064:',bd=4,bg="black",fg="white").place(x=300,y=140)
        pais=Label(self.ventana2,text='ESPAÑA',bd=4,bg="black",fg="white").place(x=300,y=170)
        modelo=Label(self.ventana2,text='2018',bd=4,bg="black",fg="white").place(x=300,y=200)
        estado=Label(self.ventana2,text='Agotado',bd=4,bg="black",fg="white").place(x=300,y=230)
        consumo=Label(self.ventana2,text='2,40V',bd=4,bg="black",fg="white").place(x=300,y=260)
        sensores=Label(self.ventana2,text='LUZ-PROXIMIDAD',bd=4,bg="black",fg="white").place(x=300,y=290)
        peso=Label(self.ventana2,text='800KG',bd=4,bg="black",fg="white").place(x=300,y=320)
        baterias=Label(self.ventana2,text='4',bd=4,bg="black",fg="white").place(x=300,y=350)
        tension=Label(self.ventana2,text='0,60V',bd=4,bg="black",fg="white").place(x=300,y=380)
        eficiencia=Label(self.ventana2,text='8',bd=4,bg="black",fg="white").place(x=300,y=410)
        temporada=Label(self.ventana2,text='2019',bd=4,bg="black",fg="white").place(x=300,y=440)
        ppB=Label(self.ventana2,text='3',bd=4,bg="black",fg="white").place(x=300,y=470)
        self.ventana2.mainloop()
        
    def revisar(self,x):
        if x==1:
            self.ventana1()
        if x==2:
            self.ventana2()

                
        

    def Ventana_About(self):
        #           _____________________________
        #__________/CONSTRUCTOR DE VENTANA
        self.Root_Main.title("about")
        self.Root_Main.config(width=1200,height=800)
        Label_Fondo = Label(self.Root_Main,image= self.imagen_Main).place(x=0,y=0)
        Buttont = Button(self.Root_Main, text = "MAIN",font=("Comic Sans MS",10),justify=CENTER,bg="#800000",fg="white",command = self.devolver_ventana_principal).place(x=1150,y=0)
        
    def devolver_ventana_principal(self):
        self.Root_Main.destroy()
        self.Main()

    def Ventana_TestDrive(self):
        self.Root_Main.title("Formula 1 - ADJ")
        self.Root_Main.config(bg="gray",width=1200,height=800)
        self.Root_Main.resizable(width=0,height=0)
        
        Label_Fondo_TestDrive = Label( self.Root_Main, image = self.Fondo_TestDrive, bd =0).place(x=0,y=0)
        Label_Volante = Label( self.Root_Main, image = self.Volante_TestDrive, bd =0).place(x=744,y=174)
        Label_Escuderia = Label( self.Root_Main, text = "                  PROPORSCHE2k19                  ", font = ("Comic Sans MS",6), relief = "sunken", bg = "black", fg = "white").place(x=743,y=248)
        Label_Dir_Izq_Off = Label( self.Root_Main, image = self.Dir_Izq_Off_TestDrive, bd =0).place(x=348,y=195)
        Label_Dir_Der_Off = Label( self.Root_Main, image = self.Dir_Der_Off_TestDrive, bd =0).place(x=505,y=195)
        Label_Bateria = Label( self.Root_Main, image = self.bateria_llena_TestDrive, bd =0).place(x=812,y=205)
        Button_Moon = Button( self.Root_Main, image = self.sun_TestDrive, bd = 0,command = lambda:self.thread_contar(Thread)).place(x=810,y=174)
        
        Buttont = Button(self.Root_Main,bg="#800000",fg="white", text = "MAIN",font=("Comic Sans MS",10),justify=CENTER,command = self.devolver_ventana_principal).place(x=1150,y=0)
        Button_Pedal_Clutch_TestDrive = Button( self.Root_Main, image = self.Pedal_Clutch_TestDrive, bd=0, command = lambda:self.Gears(Thread)).place(x=245,y=440)
        Button_Pedal_Break_TestDrive = Button( self.Root_Main, image = self.Pedal_Break_TestDrive, command = lambda:self.pwm_control(Thread,3), bd=0).place(x=400,y=450)
        Button_Pedal_Accelerator_TestDrive = Button( self.Root_Main, image = self.Pedal_Accelerator_TestDrive, command = lambda:self.pwm_control(Thread,4), bd=0).place(x=514,y=440)
        
        Button_Palanca_Dir_Izq_TestDrive = Button( self.Root_Main, image = self.Palanca_Dir_Izq_TestDrive, bd=0, command =lambda:self.thread_direccion_izquierda(Thread)).place(x=275,y=298)
        Button_Palanca_Dir_Der_TestDrive = Button( self.Root_Main, image = self.Palanca_Dir_Der_TestDrive, bd=0, command =lambda:self.thread_direccion_derecha(Thread)).place(x=515,y=298)
        Button_Emergency_TestDrive = Button( self.Root_Main, image = self.Emergency_TestDrive, bd=0, command = lambda:self.thread_parqueo(Thread,1)).place(x=152,y=238)
        
        Button_Headlights_On_TestDrive1 = Button( self.Root_Main, image = self.Headlights_On_TestDrive, command = self.Frontales_Off, bd =0).place(x=148,y=193)
        Button_Headlights_Off_TestDrive = Button( self.Root_Main, image = self.Headlights_Off_TestDrive, command = self.Frontales_On, bd =0).place(x=148,y=193)
        
        Button_Winner_TestDrive = Button( self.Root_Main, image = self.Winner_TestDrive, bd=0).place(x=833,y=174)
        
        Button_CIRCLE_Off_TestDrive = Button( self.Root_Main, image =self. CIRCLE_Off_TestDrive, bd=0, command = lambda:self.seleccion_moviento(0)).place(x=679,y=218)
        Button_ZIGZAG_Off_TestDrive = Button( self.Root_Main, image = self.ZIGZAG_Off_TestDrive, bd=0, command = lambda:self.seleccion_moviento(1)).place(x=698,y=170)
        Button_INFINITE_Off_TestDrive = Button( self.Root_Main, image = self.INFINITE_Off_TestDrive, bd=0, command = lambda:self.seleccion_moviento(2)).place(x=672,y=170)
        Button_CUSTOM_Off_TestDrive = Button( self.Root_Main, image = self.CUSTOM_Off_TestDrive, bd=0, command = lambda:self.seleccion_moviento(3)).place(x=679,y=256)
        
        Button_Girar_D = Button( self.Root_Main, bd=0, image = self.Girar_D_TestDrive, command = lambda:self.thread_girar_derecha(Thread)).place(x=515,y=220)
        Button_Girar_I = Button( self.Root_Main, bd=0, image = self.Girar_I_TestDrive, command = lambda:self.thread_girar_izquierda(Thread)).place(x=312,y=222)
        Button_Girar_0 = Button( self.Root_Main, bd=0, image = self.Girar_0_TestDrive, command = lambda:self.thread_posicion_0(Thread)).place(x=416,y=360)

        
        self.Root_Main.mainloop()
        #           ____________________________
        #__________/PWM
    def Gears(self,Thread):
        Button_Drive_TestDrive = Button( self.Root_Main, image = self.Drive_TestDrive, bd=0, command = lambda:self.pwm_control(Thread,1)).place(x=865,y=340)
        Button_Reverse_TestDrive = Button( self.Root_Main, image = self.Reverse_TestDrive, bd=0, command = lambda:self.pwm_control(Thread,2)).place(x=865,y=367)
        self.pwm_controller = "Ninguno"
    def pwm(self):
        print(self.Pedal_TestDrive,self.pwm_controller,self.velocidad_TestDrive)
        if(self.Pedal_TestDrive=="avanzar" and self.pwm_controller=="Drive"):
            x = 0
            while(x<1 and self.velocidad_TestDrive<1020):
                self.velocidad_TestDrive+=255
                print(self.velocidad_TestDrive)
                comando = "pwm:"+str(self.velocidad_TestDrive)+";"
                t = threading.Thread(target = self.send(comando))
                t.start()
                time.sleep(0.01)
                x+=1     
        if(self.Pedal_TestDrive=="retroceder" and self.pwm_controller=="Drive"):
            self.velocidad_TestDrive = 0
            comando = "pwm:"+str(self.velocidad_TestDrive)+";"
            t = threading.Thread(target = self.send(comando))
            t.start()
            print(self.velocidad_TestDrive)
                
        if(self.Pedal_TestDrive=="avanzar" and self.pwm_controller=="Reverse"):
            x = 0
            while(x<1 and self.velocidad_TestDrive>-1020):
                self.velocidad_TestDrive-=255
                print(self.velocidad_TestDrive)
                comando = "pwm:"+str(self.velocidad_TestDrive)+";"
                t = threading.Thread(target = self.send(comando))
                t.start()
                time.sleep(0.01)
                x+=1 
                
                
                
        if(self.Pedal_TestDrive=="retroceder" and self.pwm_controller=="Reverse"):
            self.velocidad_TestDrive = 0
            comando = "pwm:"+str(self.velocidad_TestDrive)+";"
            t = threading.Thread(target = self.send(comando))
            t.start()
            print(self.velocidad_TestDrive)    
        else:
            print("El auto esta en Neutral")
            
    def pwm_control(self,Thread,Control):
        if(Control==1):
            self.pwm_controller = "Drive"
            
            print(self.pwm_controller)
        elif(Control==2):
            self.pwm_controller = "Reverse"
            print(self.pwm_controller)
        elif(Control==3):
            self.Pedal_TestDrive = "retroceder"
            print(self.Pedal_TestDrive)
            t = threading.Thread(target = self.pwm())
            t.start()
        elif(Control==4):
            self.Pedal_TestDrive = "avanzar"
            print(self.Pedal_TestDrive)
            t = threading.Thread(target = self.pwm())
            t.start() 
        else:
            print("El auto esta en Neutral")                                              
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
    def contar(self):
        x=0
        while(x>=0):
            print(x)
            comando = "lx:;"
            t = threading.Thread(target = self.send(comando))
            t.start()
            time.sleep(2)
            x+=1
    def thread_contar(self,Thread):
        p = threading.Thread(target = self.contar)
        p.start()
        #           ____________________________
        #__________/DIRECCION             
    def girar_derecha(self):
        x=0
        while(x<1):
            Button_Girar_D = Button( self.Root_Main, bd=0, image = self.Girar_D_On_TestDrive).place(x=515,y=220)
            Label_Volante = Label( self.Root_Main, image = self.Volante_TestDrive, bd =0).place(x=744,y=174)
            time.sleep(0.3)
            Label_Volante = Label( self.Root_Main, image = self.Volante_D_50_TestDrive , bd =0).place(x=744,y=174)
            time.sleep(0.3)
            Button_Girar_D = Button( self.Root_Main, bd=0, image = self.Girar_D_TestDrive, command = lambda:self.thread_girar_derecha(Thread)).place(x=515,y=220)
            Label_Volante = Label( self.Root_Main, image = self.Volante_D_90_TestDrive, bd =0).place(x=744,y=174)
            
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
            Button_Girar_I = Button( self.Root_Main, bd=0, image = self.Girar_I_On_TestDrive).place(x=312,y=222)
            Label_Volante = Label( self.Root_Main, image = self.Volante_TestDrive, bd =0).place(x=744,y=174)
            time.sleep(0.3)
            Label_Volante = Label( self.Root_Main, image = self.Volante_I_50_TestDrive, bd =0).place(x=744,y=174)
            time.sleep(0.3)
            Button_Girar_I = Button( self.Root_Main, bd=0, image = self.Girar_I_TestDrive, command = lambda:self.thread_girar_izquierda(Thread)).place(x=312,y=222)
            Label_Volante = Label( self.Root_Main, image = self.Volante_I_90_TestDrive, bd =0).place(x=744,y=174)
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
            Label_Volante = Label( self.Root_Main, image = self.Volante_TestDrive, bd =0).place(x=744,y=174)
            Button_Girar_0 = Button( self.Root_Main, bd=0, image = self.Girar_0_On_TestDrive, command = lambda:self.thread_posicion_0(Thread)).place(x=416,y=360)
            time.sleep(1)
            Button_Girar_0 = Button( self.Root_Main, bd=0, image = self.Girar_0_TestDrive, command = lambda:self.thread_posicion_0(Thread)).place(x=416,y=360)
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
        Button_Headlights_On_TestDrive = Button( self.Root_Main, image = self.Headlights_On_TestDrive, bd =0, command = self.Frontales_Off).place(x=148,y=193)
        comando = self.frontales_On_TestDrive 
        t = threading.Thread(target = self.send(comando))
        t.start()
       
    def Frontales_Off(self):
        print("Headlights Off")
        Button_Headlights_Off_TestDrive = Button( self.Root_Main, image = self.Headlights_Off_TestDrive, bd =0, command = self.Frontales_On).place(x=148,y=193)
        comando = self.frontales_Off_TestDrive 
        t = threading.Thread(target = self.send(comando))
        t.start()
        #           ____________________________
        #__________/DIRECCIONALES
    def Dir_Der(self):
        x=0
        while(x<8):
            print("Dir Derecha On")
            Label_Dir_Der_On = Label( self.Root_Main, image = self.Dir_Der_On_TestDrive, bd =0).place(x=505,y=195)
            time.sleep(0.5)
            Label_Dir_Der_Off = Label( self.Root_Main, image = self.Dir_Der_Off_TestDrive, bd =0).place(x=505,y=195)
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
            Label_Dir_Izq_On = Label( self.Root_Main, image = self.Dir_Izq_On_TestDrive, bd =0).place(x=348,y=195)
            time.sleep(0.5)
            Label_Dir_Izq_Off = Label( self.Root_Main, image = self.Dir_Izq_Off_TestDrive, bd =0).place(x=348,y=195)
            time.sleep(0.5)
            x+=1
    def thread_direccion_izquierda(self,Thread):
        p = threading.Thread(target = self.Dir_Izq)
        p.start()
        comando = self.direccional_izq_TestDrive 
        t = threading.Thread(target = self.send(comando))
        t.start()
    def Emergency(self):
        Button_Emergency_TestDrive = Button( self.Root_Main, image = self.Emergency_TestDrive, bd=0, command = lambda:self.thread_parqueo(Thread,0)).place(x=152,y=238)
        x=0
        while(x<8):
            print("Emergency On")
            Label_Dir_Izq_On = Label( self.Root_Main, image = self.Dir_Izq_On_TestDrive, bd =0).place(x=348,y=195)
            Label_Dir_Der_On = Label( self.Root_Main, image = self.Dir_Der_On_TestDrive, bd =0).place(x=505,y=195) 
            time.sleep(0.5)
            Label_Dir_Izq_Off = Label( self.Root_Main, image = self.Dir_Izq_Off_TestDrive, bd =0).place(x=348,y=195)
            Label_Dir_Der_Off = Label( self.Root_Main, image = self.Dir_Der_Off_TestDrive, bd =0).place(x=505,y=195)
            time.sleep(0.5)
            x+=1 
    def Emergency_Off(self):
        Button_Emergency_TestDrive = Button( self.Root_Main, image = self.Emergency_TestDrive, bd=0, command = lambda:self.thread_parqueo(Thread,1)).place(x=152,y=238)
        print("Emergency Off")
        Label_Dir_Izq_Off = Label( self.Root_Main, image = self.Dir_Izq_Off_TestDrive, bd =0).place(x=348,y=195)
        Label_Dir_Der_Off = Label( self.Root_Main, image = self.Dir_Der_Off_TestDrive, bd =0).place(x=505,y=195)
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
            Button_CIRCLE_On_TestDrive = Button( self.Root_Main, image = self.CIRCLE_On_TestDrive, bd=0).place(x=679,y=218)
            time.sleep(0.5)
            Button_CIRCLE_Off_TestDrive = Button( self.Root_Main, image = self.CIRCLE_Off_TestDrive, bd=0, command = lambda:self.seleccion_moviento(0)).place(x=679,y=218)
            time.sleep(0.5)
            x+=1    
    def zigzag_cambio(self):
        x=0
        while(x<5):
            Button_ZIGZAG_On_TestDrive = Button( self.Root_Main, image = self.ZIGZAG_On_TestDrive, bd=0).place(x=698,y=170)
            time.sleep(0.5)
            Button_ZIGZAG_Off_TestDrive = Button( self.Root_Main, image = self.ZIGZAG_Off_TestDrive, bd=0, command = lambda:self.seleccion_moviento(1)).place(x=698,y=170)
            time.sleep(0.5)
            x+=1
    def infinito_cambio(self):
        x=0
        while(x<4):
            Button_INFINITE_On_TestDrive = Button( self.Root_Main, image = self.INFINITE_On_TestDrive, bd=0).place(x=672,y=170)
            time.sleep(0.5)
            Button_INFINITE_Off_TestDrive = Button( self.Root_Main, image = self.INFINITE_Off_TestDrive, bd=0, command = lambda:self.seleccion_moviento(2)).place(x=672,y=170)
            time.sleep(0.5)
            x+=1
    def especial_cambio(self):
        x=0
        while(x<1):
            Button_CUSTOM_Off_TestDrive = Button( self.Root_Main, image = self.CUSTOM_Off_TestDrive, bd=0, command = lambda:self.seleccion_moviento(3)).place(x=679,y=256)
            time.sleep(0.3)
            i=0
            while(i<3):
                    Button_CUSTOM1_On_TestDrive = Button( self.Root_Main, image = self.CUSTOM1_On_TestDrive, bd=0).place(x=679,y=256)
                    time.sleep(0.3)
                    Button_CUSTOM2_On_TestDrive = Button( self.Root_Main, image = self.CUSTOM2_On_TestDrive, bd=0).place(x=679,y=256)
                    time.sleep(0.3)
                    Button_CUSTOM3_On_TestDrive = Button( self.Root_Main, image = self.CUSTOM3_On_TestDrive, bd=0).place(x=679,y=256)
                    time.sleep(0.3)
                    i+=1
            Button_CUSTOM_Off_TestDrive = Button( self.Root_Main, image = self.CUSTOM_Off_TestDrive, bd=0, command = lambda:self.seleccion_moviento(3)).place(x=679,y=256)
            x+=1


#           ____________________________
#__________/INICIAR

o = Main_Interface()
o.Main()






