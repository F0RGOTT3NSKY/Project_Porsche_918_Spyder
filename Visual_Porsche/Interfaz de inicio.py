## VENTANA DE INICIO ##

from tkinter import *
import random
from random import randint

 


def ventana_principal():
    
    root=Tk()
    root.title("Formula 1 - ADJ")
    porsche=PhotoImage(file='spyder.png')
    root.config(bg="#8B0000",width="1200", height="800")
    label_de_imagen=Label(root,image=porsche).place(x=0,y=0)
    root.resizable(height=0,width=0)
    icono=root.iconbitmap('f1logo.ico') 
    f1=PhotoImage(file='f1mini.gif')
    logo=Label(root,image=f1).place(x=10,y=10)

    #### LABELS PERTENECIENTES A LA VENTANA DE ORIGEN #####

    escuderia=Label(root,text="Nombre de Escuderia:",font='helvetica 12',justify=CENTER,width="17",height="3",bg="black",fg="white")
    escuderia.place(x=10,y=150)

    Ubicacion=Label(root,text="Ubicacion:",font='helvetica 12',width="17",height="3",bg="black",fg="white")
    Ubicacion.place(x=10,y=220)

    Patrocinadores=Label(root,text="Patrocinadores:",font='helvetica 12',width="17",height="3",bg="black",fg="white")
    Patrocinadores.place(x=10,y=290)

     
    escuderia_nombre=Label(root,text="PROPORSCHE2k19",font='helvetica 12',width="17",height="3",bg="#8B0000",fg="white",relief="groove")
    escuderia_nombre.place(x=175,y=150)

    pais_ubicacion=Label(root,text="COSTA RICA",font='helvetica 12',width="17",height="3",bg="#8B0000",fg="white",relief="groove")
    pais_ubicacion.place(x=175,y=220)

    patrocinador_imagen=PhotoImage(file='SHELL_mini.gif')
    patrocinador1=Label(root,image=patrocinador_imagen,relief="solid")
    patrocinador1.place(x=175,y=290)

    patrocinador2_imagen=PhotoImage(file='firelli_mini.gif')
    patrocinador2=Label(root,image=patrocinador2_imagen,relief="solid")
    patrocinador2.place(x=300,y=290)

    patrocinador3_imagen=PhotoImage(file='marlboro_mini.gif')
    patrocinador3=Label(root,image=patrocinador3_imagen,relief="solid")
    patrocinador3.place(x=505,y=290)

    '''
    porsche=PhotoImage(file='spyder.png')
    ima_porsche=Label(root,image=porsche,bd=0).place(x=700,y=0)
    '''

    scrollbar = Scrollbar(root)
    scrollbar.place(x=50,y=600)

    def leer():
       
        file=open('porsche_datos.txt','r')
        texto=file.read()
        datos=eval(texto)
        file.close()
        return datos

    listbox = Listbox(root, yscrollcommand=scrollbar.set,bg="black",fg="white")

    pilotos=leer()
    x=random.randint(0,9)
    for i in range(0,len(pilotos)-x):
        listbox.insert(END,pilotos[i][0])
    listbox.place(x=100,y=600)

    scrollbar.config(command=listbox.yview)



    scrollbar1 = Scrollbar(root)
    scrollbar1.place(x=250,y=600)

    listbox = Listbox(root, yscrollcommand=scrollbar.set,bg="#8B0000",fg="white")



    x=random.randint(0,9)
    for i in range(0,len(pilotos)-x):
        listbox.insert(END,pilotos[i][1])
    listbox.place(x=300,y=600)

    scrollbar1.config(command=listbox.yview)


    def Ventana_about():
        root.destroy()
        about=Tk()
        about.title("about")
        about.config(width=1200,height=800)
        imagen=PhotoImage(file='about.gif')
        about_fondo=Label(about,image=imagen).pack()
        def devolver_ventana_principal():
            about.destroy()
            return ventana_principal()
        devolver=PhotoImage(file='girar_izquierda_press.png')
        boton_de_devolver=Button(about,image=devolver,command=devolver_ventana_principal,relief="raised").place(x=1310,y=700)
        
        about.mainloop()



        
    ### BOTONES PERTENECIENTES A LA VENTANA DE ORIGEN #### 
    minim = Button(root, text="MINIMIZAR", command=root.iconify,justify=CENTER,bg="#454545",fg="white",relief="raised",bd=15)
    minim.place(x=1100,y=0)

    exit = Button(root, text="SALIR", command=root.destroy,justify=CENTER,bg="#454545",fg="white",relief="raised",bd=15)
    exit.place(x=1030,y=0)

    tabla = Button(root, text="TABLA DE POSICIONES",font=("Comic Sans MS",10),width=18, justify=CENTER,bg="#800000",fg="white",relief="raised",bd=15)
    tabla.place(x=1020,y=100)

    historial = Button(root, text="HISTORIAL DE AUTOS",font=("Comic Sans MS",10),width=18 ,justify=CENTER,bg="#454545",fg="white",relief="raised",bd=15)
    historial.place(x=1020,y=200)


    drive = Button(root, text="TEST DRIVE",width=18,font=("Comic Sans MS",10),justify=CENTER,bg="#800000",fg="white",relief="raised",bd=15)
    drive.place(x=1020,y=300)

    drive = Button(root, text="TEST DRIVE",width=18,font=("Comic Sans MS",10),justify=CENTER,bg="#800000",fg="white",relief="raised",bd=15)
    drive.place(x=820,y=220)


    editar = Button(root, text="EDITAR", width=18,font=("Comic Sans MS",10),justify=CENTER,bg="#454545",fg="white",relief="raised",bd=15)
    editar.place(x=1020,y=400)

    about = Button(root, text="MÁS...",font=("Comic Sans MS",10),width=18,command=Ventana_about,justify=CENTER,bg="#800000",fg="white",relief="raised",bd=15)
    about.place(x=1020,y=500)
    root.mainloop()




ventana_principal()






