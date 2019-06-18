#           _____________________________
#__________/BIBLIOTECAS
from tkinter import *


#           _____________________________
#__________/VARIABLES GLOBALES
root=Tk()
fondo=PhotoImage(file='spyder.png')
icono=root.iconbitmap('f1logo.ico')
patrocinador_imagen=PhotoImage(file='SHELL_mini.gif')
patrocinador2_imagen=PhotoImage(file='firelli_mini.gif')
patrocinador3_imagen=PhotoImage(file='marlboro_mini.gif')
f1=PhotoImage(file='f1mini.gif')

root, fondo, icono, patrocinador_imagen, patrocinador2_imagen, patrocinador3_imagen
#           _____________________________
#__________/VENTANA PRINCIPAL
class Main_Interface:
    def __init__(self,root_Main, fondo_Main, icono_Main, patrocinador_imagen_Main, patrocinador2_imagen_Main, patrocinador3_imagen_Main):
        #           _____________________________
        #__________/VARIABLES PRIVADAS
        self.root_Main = root_Main
        self.fondo_Main = fondo_Main
        self.icono_Main = icono_Main
        self.patrocinador_imagen_Main = patrocinador_imagen_Main
        self.patrocinador2_imagen_Main = patrocinador2_imagen_Main
        self.patrocinador3_imagen_Main = patrocinador3_imagen_Main
        #           _____________________________
        #__________/CONSTRUCTOR DE VENTANA
        root.title("Formula 1 - ADJ")
        root.config(bg="#8B0000",width="1200", height="800")
        label_de_imagen=Label(root,image=fondo).place(x=0,y=0)
        root.resizable(height=0,width=0)
        
        escuderia=Label(root,text="Nombre de Escuderia:",font='helvetica 12',justify=CENTER,width="17",height="3",bg="black",fg="white").place(x=10,y=150)
        Ubicacion=Label(root,text="Ubicacion:",font='helvetica 12',width="17",height="3",bg="black",fg="white").place(x=10,y=220)
        Patrocinadores=Label(root,text="Patrocinadores:",font='helvetica 12',width="17",height="3",bg="black",fg="white").place(x=10,y=290)
        escuderia_nombre=Label(root,text="PROPORSCHE2k19",font='helvetica 12',width="17",height="3",bg="#8B0000",fg="white",relief="groove").place(x=175,y=150)
        pais_ubicacion=Label(root,text="COSTA RICA",font='helvetica 12',width="17",height="3",bg="#8B0000",fg="white",relief="groove").place(x=175,y=220)
        patrocinador1=Label(root,image=patrocinador_imagen,relief="solid").place(x=175,y=290)
        patrocinador2=Label(root,image=patrocinador2_imagen,relief="solid").place(x=300,y=290)
        patrocinador3=Label(root,image=patrocinador3_imagen,relief="solid").place(x=505,y=290)
    
        minim = Button(root, text="MINIMIZAR", command=root.iconify,justify=CENTER,bg="#454545",fg="white",relief="raised",bd=15).place(x=1030,y=10)
        salida = Button(root, text="SALIR", command=root.destroy,justify=CENTER,bg="#454545",fg="white",relief="raised",bd=15).place(x=950,y=10)
        tabla = Button(root, text="TABLA DE POSICIONES",font=("Comic Sans MS",10),width=18, justify=CENTER,bg="#800000",fg="white",relief="raised",bd=15).place(x=950,y=100)
        historial = Button(root, text="HISTORIAL DE AUTOS",font=("Comic Sans MS",10),width=18 ,justify=CENTER,bg="#454545",fg="white",relief="raised",bd=15).place(x=950,y=160)
        drive = Button(root, text="TEST DRIVE",width=18,font=("Comic Sans MS",10),justify=CENTER,bg="#800000",fg="white",relief="raised",bd=15).place(x=950,y=220)
        editar = Button(root, text="EDITAR", width=18,font=("Comic Sans MS",10),justify=CENTER,bg="#454545",fg="white",relief="raised",bd=15).place(x=950,y=280)
        about = Button(root, text="MÁS...",font=("Comic Sans MS",10),width=18,justify=CENTER,bg="#800000",fg="white",relief="raised",bd=15).place(x=950,y=340)


#           ____________________________
#__________/INICIAR
Main_Interface(root, fondo, icono, patrocinador_imagen, patrocinador2_imagen, patrocinador3_imagen)






