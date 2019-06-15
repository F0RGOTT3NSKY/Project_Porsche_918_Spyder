from tkinter import*
import os

#funcion para cargar imagen
def cargar_imagen(nombre):
    ruta = os.path.join('Images',nombre)
    imagen = PhotoImage(file = ruta)
    return imagen

#creación de la ventana principal
ventana=Tk()
ventana.title("About")
ventana.minsize(1485, 800)
ventana.resizable(width=NO,height=NO)

#creación del canvas
contenedor1=Canvas(ventana,width=1485,height=800,bg="BLACK")
contenedor1.place(x=-2,y=-2)

#colocar imagenes de la patalla de inicio
inicio1 = cargar_imagen("about.gif")
Labelinicio1= Label(contenedor1, image = inicio1, bg = "BLACK")
Labelinicio1.place(x=0,y=0)
