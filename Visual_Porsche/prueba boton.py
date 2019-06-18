import tkinter
from tkinter import *
import time
import threading

root=Tk()
root.title("Formula 1 - ADJ")
root.config(bg="gray",width=500,height=500)
root.resizable(width=0,height=0)


on_off=PhotoImage(file="off.png")
luces_frontales=Button(root,image=on_off).place(x=0,y=0)
luces_frontales.bind('<Button-1>', print1())



def print1():
        print("hola")
