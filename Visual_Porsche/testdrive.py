import tkinter as tk
from tkinter import *
import time
import threading 
### ventana principal ###

def test_drive():
    root=Tk()
    root.title("Formula 1 - ADJ")
    root.config(bg="black",width=1485,height=900)
    root.resizable(width=0,height=0)
    fondo=PhotoImage(file='porsche_dash.gif')
    label_de_imagen=Label(root,image=fondo).place(x=0,y=0)
    icono=root.iconbitmap('f1logo.ico')
    ## VELOCIMETRO ###
    velocimetro_neon=PhotoImage(file='velocimetro.png')
    velocimetro=Label(root,image=velocimetro_neon,bg='black').place(x=388,y=91)
    ## VOLANTE EN POSICION NORMAL ## 
    volante=PhotoImage(file="volante_0.png")
    ## VOLANTE EN POSICION 50 DERECHA ##
    volante2=PhotoImage(file='volante_d_50.png')
    ## VOLANTE EN POSICION 90 DERECHA ##
    volante3=PhotoImage(file='volante_d_90.png')
    ## VOLANTE EN POSICION 50 IZQUIERDA ##
    volante4=PhotoImage(file='volante_i_50.png')
    ## VOLANTE EN POSICION 90 IZQUIERDA ##
    volante5=PhotoImage(file='volante_i_90.png')
    L_volante=Label(root,image=volante)
    L_volante.place(x=1202,y=0)





    ## DIRECCIONALES ###

    dir_default=PhotoImage(file="direccion_izquierda_default.png")        
    direccional_default=Label(root,image=dir_default).place(x=1202,y=500)

    dir_derecha_default=PhotoImage(file="direccion_derecha_default.png")        
    direccional_derecha_default=Label(root,image=dir_derecha_default).place(x=1340,y=500)


    Escuderia=Label(root,justify=CENTER,text="PROPORSCHE2k19",font=("Comic Sans MS",7),relief="sunken",bg="black",fg="white").place(x=744,y=242)

    #=======
    Escuderia=Label(root,justify=CENTER,text="PROPORSCHE2k19",font=("Comic Sans MS",7),relief="sunken",bg="black",fg="white").place(x=746,y=244)
    ## BATERIAS  ###
    bateria_llena=PhotoImage(file='bateria_llena.png')
    llena=Label(root,image=bateria_llena,bd=0).place(x=857,y=205)


    ## LUZ Y OSCURIDAD ##
    moon=PhotoImage(file='luna.png')
    luna=Label(root,image=moon,bd=0).place(x=867,y=176)

    sol=PhotoImage(file='sol.png')


    ### TECLAS ### 
    def R(event):
        if event.keysym=='Right':
            return thread_girar_derecha()
    def L(event):
        if event.keysym=='Left':
            return thread_girar_izquierda()
    def Arriba(event):
        return thread_posicion_0()





    def cambio2(event):
        return thread_sol()
            
    def cambio(event):
        return thread_luz_oscuridad()    
            


    root.bind_all("<KeyPress-Right>",R)
    root.bind_all("<KeyPress-Left>",L)
    root.bind_all("<KeyPress-Up>",Arriba)
    root.bind_all("<KeyPress-s>",cambio)
    root.bind_all("<KeyPress-l>",cambio2)

    imaCounter = 0


    def adelante(event):
        imaCounter = 0

        if imaCounter >=200:
            imalabel.config(text="200kmph",font=("Comic Sans MS",7))
        else:
            
            imaCounter +=0.8
        
            imalabel.config(text=int(imaCounter),font=("Comic Sans MS",7))

    def atras(event):
        imaCounter = 0

        if imaCounter <=-200:
            imalabel.config(text="-200kmph",font=("Comic Sans MS",7))
        else:
            
            imaCounter -=0.8
        
            imalabel.config(text=int(imaCounter),font=("Comic Sans MS",7))

    def detener(event):
        imaCounter = 0

        if imaCounter >0:
            if imaCounter==0:
                imalabel.config(text="0",font=("Comic Sans MS",7))
            else:
                imaCounter -=0.8
                imalabel.config(text=int(imaCounter),font=("Comic Sans MS",7))
        else:
            if imaCounter==0:
                imalabel.config(text="0",font=("Comic Sans MS",7))
            else:
                imaCounter +=0.8
                imalabel.config(text=int(imaCounter),font=("Comic Sans MS",7))
            
                
        
    root.bind_all('<KeyPress-w>',adelante)
    root.bind_all('<KeyPress->s',atras)
    root.bind('<space>',detener) 

    imalabel=Label(root,text='0',bd=0,bg="#0B173B",fg='white',font=("Comic Sans MS",7))
    imalabel.place(x=418,y=130)


        ### botones con imagenes ###
    pedal_closh=PhotoImage(file="pedal.png")
    closh=Button(root,bd=0,image=pedal_closh).place(x=245,y=440)
    pedal_freno=PhotoImage(file="freno.png")
    freno=Button(root,bd=0,image=pedal_freno).place(x=400,y=440)




    ##VELOCIDAD ###


    pedal_gas=PhotoImage(file="gas.png")
    gas=Button(root,bd=0,image=pedal_gas).place(x=514,y=440)


    palanca_direccional=PhotoImage(file="direccional.png")
    direccional_izquierda=Button(root,bd=0,image=palanca_direccional,command=lambda :thread_direccion_izquierda()).place(x=275,y=298)

    palanca_direccional2=PhotoImage(file="direccional_derecha.png")
    direccional_derecha=Button(root,bd=0,image=palanca_direccional2,command=lambda :thread_direccion_derecha()).place(x=515,y=298)


    ### BOTONES DE MOVIMIENTOS ESPECIALES Y FUNCION ##

    ### CELEBRACION ####

    ganador=PhotoImage(file="celebracion.gif")
    celebracion=Button(root,image=ganador).place(x=1358,y=282)

    #### MOV_ESPECIAL ########### 
    mov_especial=PhotoImage(file='movimiento_especial_apagado.png')
    especial=Button(root,image=mov_especial,command=lambda: thread_especial()).place(x=955,y=710)
           
    #BOTONES DE DIRECCION #


    ## GIRAR HACIA LA DERECHA ### 
    girar_D=PhotoImage(file='girar_derecha.png')
    girar_derecha=Button(root,bd=0,image=girar_D,command=lambda: thread_girar_derecha()).place(x=1385,y=600)

    ### GIRAR HACIA LA IZQUIERDA ### 
    girar_I=PhotoImage(file='girar_izquierda.png')
    girar_izquierda=Button(root,bd=0,image=girar_I,command=lambda: thread_girar_izquierda()).place(x=1203,y=600)

    ### PONER EN DIRECCION 0 ####     
    direccion_0=PhotoImage(file='direccion_0.png')
    girar_none=Button(root,bd=0,image=direccion_0,command=lambda: thread_posicion_0()).place(x=1310,y=600)

    ### CIRCULO ###

    circulo=PhotoImage(file="circulo_apagado.png")
    mov_Circulo= tk.Button(root, image=circulo,command=lambda: thread_circulo()).place(x=670,y=248)


                    
                    
     
    ######## ZIGZAG #########  

    zigzag=PhotoImage(file="zigzag_apagado.png")
    mov_zigzag=Button(root,image=zigzag,command=lambda: thread_zigzag()).place(x=938,y=185)



    ######## INFINITO #########  
    infinito=PhotoImage(file="infinito_apagado.png")
    mov_infinito=Button(root, image=infinito,command=lambda: thread_infinito()).place(x=670,y=185)
    ######################################################################### BOTONES PARA LAS FUNCIONES DEL CARRO ########################################## 
    ## BOTON INFINITO ##

    boton_infinito=Button(root,text='Sensor de luces',bd=0,fg="white",bg="black",command=lambda: thread_contar()).place(x=10,y=0)
    ## LUCES DE PARQUEO ### 

    emergencia=PhotoImage(file="emergencia_mini.png")
    boton_luces_de_emergencia=Button(root,image=emergencia,command=lambda :thread_parqueo()).place(x=420,y=370)

    # BOTON PARA IR ADELANTE# 
    flecha_arriba=PhotoImage(file="flecha_arriba.png")
    ir_adelante=Button(root,image=flecha_arriba).place(x=865,y=340)

    # BOTON PARA REVERSA ##
    flecha_abajo=PhotoImage(file="flecha_abajo.png")
    ir_atras=Button(root,image=flecha_abajo).place(x=865,y=367)

    ################## FUNCIONES PARA LOS BOTONES Y LABELS ##########################################################################################################
    #### FUNCION PARA LAS LUCES FRONTALES Y LOS BOTONES  ##########
    def btn_hide():
        if b1.winfo_ismapped():
            b2.place_forget()
            b1.place(x=1202,y=282)
           
        else:
            
            b1.place(x=1202, y=282)
            
    def btn_show():
        if b2.winfo_ismapped():
            b1.place_forget()
            b2.place(x=1202,y=282)
           
        else:
            
            b2.place(x=1202, y=282)
            
    ## LUCES ENCENDIDAS ###         
    on=PhotoImage(file="on.png")
    b1 = tk.Button(root,image=on,command=btn_show)
    b1.place(x=1202, y=282)
    ## LUCES APAGADAS ##
    off=PhotoImage(file="off.png")
    b2 = tk.Button(root,image=off, command=btn_hide)
    b2.place(x=1202, y=282)
    ### funcion para el direccional de la izquierda ###
        
    def direccion_izquierda():
            global dir_default
            x=0
            while(x<6):
                dir_default=PhotoImage(file='direccion_izquierda.png')
                direccional_default=Label(root,image=dir_default).place(x=1202,y=500)
                time.sleep(0.5)
                dir_default=PhotoImage(file='direccion_izquierda_default.png')
                direccional_default=Label(root,image=dir_default).place(x=1202,y=500)
                time.sleep(0.5)
                x+=1
            
    def thread_direccion_izquierda():
        p=threading.Thread(target=direccion_izquierda)
        p.start()


    ## funcion para el direccional derecha ###  
    def direccion_derecha():
            global dir_derecha_default
            x=0
            while(x<6):
                dir_derecha_default=PhotoImage(file='direccion_derecha.png')
                direccional_derecha_default=Label(root,image=dir_derecha_default).place(x=1340,y=500)
                time.sleep(0.5)
                dir_derecha_default=PhotoImage(file="direccion_derecha_default.png")
                direccional_derecha_default=Label(root,image=dir_derecha_default).place(x=1340,y=500)
                time.sleep(0.5)
                x+=1
            
    def thread_direccion_derecha():
        p=threading.Thread(target=direccion_derecha)
        p.start()


    ##### funcion para luces de parqueo ####### 
    def luces_parque():
            global dir_default,dir_derecha_default
            x=0
            while(x<6):
                dir_default=PhotoImage(file='direccion_izquierda.png')
                direccional_default=Label(root,image=dir_default).place(x=1202,y=500)
                dir_derecha_default=PhotoImage(file='direccion_derecha.png')
                direccional_derecha_default=Label(root,image=dir_derecha_default).place(x=1340,y=500)
                
                time.sleep(0.5)
                
                dir_default=PhotoImage(file='direccion_izquierda_default.png')
                direccional_default=Label(root,image=dir_default).place(x=1202,y=500)
                dir_derecha_default=PhotoImage(file="direccion_derecha_default.png")
                direccional_derecha_default=Label(root,image=dir_derecha_default).place(x=1340,y=500)
                time.sleep(0.5)
                x+=1
            
    def thread_parqueo():
        p=threading.Thread(target=luces_parque)
        p.start()
        
    #### HILO PARA CAMBIO DE CIRCULO ######
    def circulo_cambio():
            global circulo
            x=0
            while(x<7):
                circulo=PhotoImage(file='circulo_encendido.png')
                mov_Circulo= tk.Button(root, image=circulo,command=lambda: thread_circulo()).place(x=670,y=248)
                time.sleep(0.5)
                circulo=PhotoImage(file="circulo_apagado.png")
                mov_Circulo= tk.Button(root, image=circulo,command=lambda: thread_circulo()).place(x=670,y=248)
                time.sleep(0.5)
                x+=1
            
    def thread_circulo():
        p=threading.Thread(target=circulo_cambio)
        p.start()
    #### HILO PARA CAMBIO DE ZIGZAG ######
    def zigzag_cambio():
            global zigzag
            x=0
            while(x<7):
                zigzag=PhotoImage(file='zigzag.png')
                mov_zigzag=Button(root,image=zigzag,command=lambda: thread_zigzag()).place(x=938,y=185)
                time.sleep(0.5)
                zigzag=PhotoImage(file="zigzag_apagado.png")
                mov_zigzag=Button(root,image=zigzag,command=lambda: thread_zigzag()).place(x=938,y=185)
                time.sleep(0.5)
                x+=1
            
    def thread_zigzag():
        p=threading.Thread(target=zigzag_cambio)
        p.start()

        
    #### HILO PARA CAMBIO DE INFINITO ######
    def infinito_cambio():
            global infinito
            x=0
            while(x<7):
                infinito=PhotoImage(file='infinito_encendido.png')
                mov_infinito=Button(root, image=infinito,command=lambda: thread_infinito()).place(x=670,y=185)
                time.sleep(0.5)
                infinito=PhotoImage(file="infinito_apagado.png")
                mov_infinito=Button(root, image=infinito,command=lambda: thread_infinito()).place(x=670,y=185)
                time.sleep(0.5)
                x+=1
            
    def thread_infinito():
        p=threading.Thread(target=infinito_cambio)
        p.start()

    #### HILO PARA CAMBIO DE ESPECIAL ######
    def especial_cambio():
            global mov_especial
            x=0
            while(x<1):
                mov_especial=PhotoImage(file='movimiento_especial_apagado.png')
                especial=Button(root,image=mov_especial,command=lambda: thread_especial()).place(x=955,y=710)
                time.sleep(0.3)
                i=0
                while(i<10):
                        
                        mov_especial=PhotoImage(file="movimiento_especial1.png")
                        especial=Button(root,image=mov_especial,command=lambda: thread_especial()).place(x=955,y=710)
                        time.sleep(0.3)
                        mov_especial=PhotoImage(file="movimiento_especial2.png")
                        especial=Button(root,image=mov_especial,command=lambda: thread_especial()).place(x=955,y=710)
                        time.sleep(0.3)
                        mov_especial=PhotoImage(file="movimiento_especial3.png")
                        especial=Button(root,image=mov_especial,command=lambda: thread_especial()).place(x=955,y=710)
                        time.sleep(0.3)
                        i+=1
                mov_especial=PhotoImage(file='movimiento_especial_apagado.png')
                especial=Button(root,image=mov_especial,command=lambda: thread_especial()).place(x=955,y=710)
                x+=1
            
    def thread_especial():
        p=threading.Thread(target=especial_cambio)
        p.start()

        
    ### HILO PARA LA POSICION 1 ####          
    def girar_derecha():
            global volante,girar_D
            x=0
            while(x<1):
                girar_D=PhotoImage(file='girar_derecha_press.png')
                girar_derecha=Button(root,bd=0,image=girar_D,command=lambda: thread_girar_derecha()).place(x=1385,y=600)
                volante=PhotoImage(file='volante_0.png')
                L_volante=Label(root,image=volante).place(x=1202,y=0)
                time.sleep(0.3)
                volante=PhotoImage(file="volante_d_50.png")
                L_volante=Label(root,image=volante).place(x=1202,y=0)
                time.sleep(0.3)
                girar_D=PhotoImage(file='girar_derecha.png')
                girar_derecha=Button(root,bd=0,image=girar_D,command=lambda: thread_girar_derecha()).place(x=1385,y=600)
                volante=PhotoImage(file='volante_d_90.png')
                L_volante=Label(root,image=volante).place(x=1202,y=0)
                
                x+=1
            
    def thread_girar_derecha():
        p=threading.Thread(target=girar_derecha)
        p.start()


        
    ### HILO PARA LA POSICION -1 ####      
    def girar_izquierda():
            global volante,girar_I
            x=0
            while(x<1):
                girar_I=PhotoImage(file='girar_izquierda_press.png')
                girar_izquierda=Button(root,bd=0,image=girar_I,command=lambda: thread_girar_izquierda()).place(x=1203,y=600)
                volante=PhotoImage(file='volante_0.png')
                L_volante=Label(root,image=volante).place(x=1202,y=0)
                time.sleep(0.3)
                volante=PhotoImage(file="volante_i_50.png")
                L_volante=Label(root,image=volante).place(x=1202,y=0)
                time.sleep(0.3)
                volante=PhotoImage(file='volante_i_90.png')
                L_volante=Label(root,image=volante).place(x=1202,y=0)
                girar_I=PhotoImage(file='girar_izquierda.png')
                girar_izquierda=Button(root,bd=0,image=girar_I,command=lambda: thread_girar_izquierda()).place(x=1203,y=600)
                
                x+=1
            
    def thread_girar_izquierda():
        p=threading.Thread(target=girar_izquierda)
        p.start()





    ### HILO PARA LA POSICION 0 ####          
    def girar_0():
            global volante,direccion_0
            x=0
            while(x<1):
                volante=PhotoImage(file='volante_0.png')
                L_volante=Label(root,image=volante).place(x=1202,y=0)
                direccion_0=PhotoImage(file='direccion_0_press.png')
                girar_none=Button(root,bd=0,image=direccion_0,command=lambda: thread_posicion_0()).place(x=1310,y=600)
                time.sleep(1)
                direccion_0=PhotoImage(file='direccion_0.png')
                girar_none=Button(root,bd=0,image=direccion_0,command=lambda: thread_posicion_0()).place(x=1310,y=600)
                
                
                
                x+=1

    def thread_posicion_0():
        p=threading.Thread(target=girar_0)
        p.start()
        
    def oscuro():
            global moon,sol
            x=0
            while(x<1):
                moon=PhotoImage(file='luna.png')
                luna=Label(root,image=moon,bd=0,bg="black").place(x=867,y=176)
                
                time.sleep(0.5)
                moon=PhotoImage(file='sol.png')
                luna=Label(root,image=moon,bd=0).place(x=867,y=176)
                
                
                
                x+=1

    def thread_luz_oscuridad():
        p=threading.Thread(target=oscuro)
        p.start()
        
    def sol():
            global moon,sol
            x=0
            while(x<1):
                moon=PhotoImage(file='sol.png')
                luna=Label(root,image=moon,bd=0).place(x=867,y=176)
                
                time.sleep(0.5)
                moon=PhotoImage(file='luna.png')
                luna=Label(root,image=moon,bg="black",bd=0).place(x=867,y=176)
                
                
                
                x+=1

    def thread_sol():
        p=threading.Thread(target=sol)
        p.start()

        
    def contar():
            
            x=0
            while(x>=0):
                
                print(x)
                time.sleep(1)
      
                
                
                
                x+=1

    def thread_contar():
        p=threading.Thread(target=contar)
        p.start()

    root.mainloop()
    ################################################################################################## FUNCIONES ##############################################################################
test_drive()
