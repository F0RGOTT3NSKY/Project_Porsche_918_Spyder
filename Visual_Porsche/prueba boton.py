import tkinter
from tkinter import *
import time
import threading

root=Tk()
root.title("Formula 1 - ADJ")
root.config(bg="gray",width=500,height=500)
root.resizable(width=0,height=0)


on_off=PhotoImage(file="on_off.png")
luces_frontales=Button(root,image=on_off,command=lambda :thread_izquierda()).place(x=0,y=0)

def izq():
        global on_off
        x=0
        while(x<6):
            on_off=PhotoImage(file='luz_alta_encendida.png')
            luces_frontales=Button(root,image=on_off,command=lambda :thread_izquierda()).place(x=0,y=0)
            time.sleep(0.5)
            on_off=PhotoImage(file='on_off.png')
            luces_frontales=Button(root,image=on_off,command=lambda :thread_izquierda()).place(x=0,y=0)
            time.sleep(0.5)
            x+=1
        
def thread_izquierda():
    p=threading.Thread(target=izq)
    p.start()
root.mainloop()
