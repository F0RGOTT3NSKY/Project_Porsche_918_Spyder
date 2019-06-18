import tkinter
from tkinter import *
import time
import threading
from threading import *
import os



class Display:
    def __init__(self):
        self.Root_Main = None
    def principal(self):
        self.__ventana = Tk()
        self.__ventana.title("GAME")
        self.__ventana.minsize(800,600)
        self.__ventana.resizable(width=NO, height=NO)
        self.__ventana.configure(background="#660920")     


x = Display()
x.principal()
