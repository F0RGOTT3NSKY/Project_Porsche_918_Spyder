import tkinter
from tkinter import *
import time
import threading 
### ventana principal ###

   
root=Tk()
root.title("Formula 1 - ADJ")
root.config(bg="gray",width=1485,height=900)
root.resizable(width=0,height=0)
fondo=PhotoImage(file='porsche_dash.gif')
label_de_imagen=Label(root,image=fondo).place(x=0,y=0)
icono=root.iconbitmap('f1logo.ico')
volante=PhotoImage(file="img.png")
L_volante=Label(root,image=volante).place(x=1202,y=0)

        




 

    ### botones con imagenes ###
pedal_closh=PhotoImage(file="pedal.png")
closh=Button(root,image=pedal_closh).place(x=245,y=440)
pedal_freno=PhotoImage(file="freno.png")
freno=Button(root,image=pedal_freno).place(x=400,y=440)
pedal_gas=PhotoImage(file="gas.png")
gas=Button(root,image=pedal_gas).place(x=514,y=440)

palanca_direccional=PhotoImage(file="direccional.png")
direccional_izquierda=Button(root,image=palanca_direccional).place(x=275,y=298)

palanca_direccional2=PhotoImage(file="direccional_derecha.png")
direccional_derecha=Button(root,image=palanca_direccional2).place(x=515,y=298)




    

emergencia=PhotoImage(file="emergencia_mini.png")
boton_luces_de_emergencia=Button(root,image=emergencia).place(x=420,y=370)


on_off=PhotoImage(file="on_off.png")
luces_frontales=Button(root,image=on_off,command=lambda :thread_izquierda()).place(x=1202,y=276)

def izq():
        global on_off
        x=0
        while(x<6):
            on_off=PhotoImage(file='luz_alta_encendida.png')
            luces_frontales=Button(root,image=on_off,command=lambda :thread_izquierda()).place(x=1202,y=276)
            time.sleep(0.5)
            on_off=PhotoImage(file='on_off.png')
            luces_frontales=Button(root,image=on_off,command=lambda :thread_izquierda()).place(x=1202,y=276)
            time.sleep(0.5)
            x+=1
        
def thread_izquierda():
    p=threading.Thread(target=izq)
    p.start()
root.mainloop()

 
 
root.mainloop()
