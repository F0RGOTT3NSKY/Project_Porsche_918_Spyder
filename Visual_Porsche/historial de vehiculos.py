from tkinter import *

def ventana_principal():
    
    vehiculos=Tk()
    vehiculos.title("historial de autos")
    icono=vehiculos.iconbitmap('f1logo.ico')
    vehiculos.resizable(width=False,height=False)
    vehiculos.config(width=1200,height=800,bg="gray")
    fondo=PhotoImage(file='fondo_para_historial.png')
    fondo_porsche=Label(vehiculos,image=fondo).place(x=0,y=0)

    devolver=PhotoImage(file='girar_izquierda_press.png')
    boton_de_devolver=Button(vehiculos,image=devolver,relief="raised").place(x=1100,y=700)

    ### BOTONES DE VEHICULOS ###

    vehiculo1=Button(vehiculos,fg="white",text="Mercedes-AMG F1 M10",bg="#f22424",relief="raised",bd=10,command=lambda: revisar(1)).place(x=70,y=10)

    vehiculo2=Button(vehiculos,fg="white",text="Ferrari 064",bg="#f22424",relief="raised",bd=10,command=lambda: revisar(2)).place(x=70,y=100)

    vehiculo3=Button(vehiculos,fg="white",text="Honda RA619H9",bg="#f22424",relief="raised",bd=10,command=lambda: revisar(3)).place(x=70,y=190)

    vehiculo4=Button(vehiculos,fg="white",text="Renault E-Tech 19",bg="#f22424",bd=10,relief="raised",command=lambda: revisar(4)).place(x=70,y=280)

    vehiculo5=Button(vehiculos,fg="white",text="Ferrari 06413",bg="#f22424",bd=10,relief="raised",command=lambda: revisar(5)).place(x=70,y=370)

    vehiculo6=Button(vehiculos,fg="white",text="Renault E-Tech 1916",bg="#f22424",bd=10,relief="raised",command=lambda: revisar(6)).place(x=900,y=10)

    vehiculo7=Button(vehiculos,fg="white",text="BWT Mercedes-AMG F1",bg="#f22424",bd=10,relief="raised",command=lambda: revisar(7)).place(x=900,y=100)

    vehiculo8=Button(vehiculos,fg="white",text="Ferrari 06426",bg="#f22424",bd=10,relief="raised",command=lambda: revisar(8)).place(x=900,y=190)

    vehiculo9=Button(vehiculos,fg="white",text="Honda RA619H28",bg="#f22424",bd=10,relief="raised",command=lambda: revisar(9)).place(x=900,y=280)

    vehiculo10=Button(vehiculos,fg="white",text="Mercedes-AMG F1 M10 EQ Power+31",bg="#f22424",bd=10,relief="raised",command=lambda: revisar(10)).place(x=900,y=370)
    def ventana1():
        ## VENTANA 1 ## 
        ventana1=Toplevel()
        ventana1.config(width=500,height=500)
        pistaIma=PhotoImage(file='pista.png')
        ventana1.resizable(width=False,height=False)
        pista=Label(ventana1,image=pistaIma).place(x=0,y=0)
        icono=ventana1.iconbitmap('f1logo.ico')
        vehiculo1=PhotoImage(file='auto1.png')
        carro1=Label(ventana1,image=vehiculo1)
        carro1.place(x=0,y=0)
        ### ESPECIFICACIONES ##
        nombre=Label(ventana1,text='nombre:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=140)
        pais=Label(ventana1,text='Pais:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=170)
        modelo=Label(ventana1,text='Modelo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=200)
        estado=Label(ventana1,text='Estado:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=230)
        consumo=Label(ventana1,text='Consumo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=260)
        sensores=Label(ventana1,text='Sensores:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=290)
        peso=Label(ventana1,text='Peso:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=320)
        baterias=Label(ventana1,text='baterias:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=350)
        tension=Label(ventana1,text='tension:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=380)
        eficiencia=Label(ventana1,text='Eficiencia:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=410)
        temporada=Label(ventana1,text='Temporada:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=440)
        ppB=Label(ventana1,text='PPB:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=470)
        
        ### RESPUESTA  ###
        nombre=Label(ventana1,text='Mercedes-AMG',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=140)
        pais=Label(ventana1,text='FINLANDIA',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=170)
        modelo=Label(ventana1,text='2019',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=200)
        estado=Label(ventana1,text='Disponible',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=230)
        consumo=Label(ventana1,text='1,29V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=260)
        sensores=Label(ventana1,text='Luz',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=290)
        peso=Label(ventana1,text='744kg',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=320)
        baterias=Label(ventana1,text='1',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=350)
        tension=Label(ventana1,text='0,29V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=380)
        eficiencia=Label(ventana1,text='8',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=410)
        temporada=Label(ventana1,text='2016',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=440)
        ppB=Label(ventana1,text='5',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=470)
        
        ventana1.mainloop()
        
    def ventana2():

        ventana2=Toplevel()
        ventana2.config(width=500,height=500,bg="black")
        icono=ventana2.iconbitmap('f1logo.ico')
        ventana2.resizable(width=False,height=False)
        pistaIma=PhotoImage(file='pista.png')
        pista=Label(ventana2,image=pistaIma).place(x=0,y=0)
        vehiculo2=PhotoImage(file='auto2.png')
        carro2=Label(ventana2,image=vehiculo2)
        carro2.place(x=0,y=0)
        nombre=Label(ventana2,text='nombre:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=140)
        pais=Label(ventana2,text='Pais:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=170)
        modelo=Label(ventana2,text='Modelo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=200)
        estado=Label(ventana2,text='Estado:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=230)
        consumo=Label(ventana2,text='Consumo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=260)
        sensores=Label(ventana2,text='Sensores:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=290)
        peso=Label(ventana2,text='Peso:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=320)
        baterias=Label(ventana2,text='baterias:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=350)
        tension=Label(ventana2,text='tension:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=380)
        eficiencia=Label(ventana2,text='Eficiencia:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=410)
        temporada=Label(ventana2,text='Temporada:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=440)
        ppB=Label(ventana2,text='PPB:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=470)
        ### RESPUESTA  ###
        nombre=Label(ventana2,text='FERRARI 064:',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=140)
        pais=Label(ventana2,text='ESPAÑA',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=170)
        modelo=Label(ventana2,text='2018',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=200)
        estado=Label(ventana2,text='Agotado',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=230)
        consumo=Label(ventana2,text='2,40V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=260)
        sensores=Label(ventana2,text='LUZ-PROXIMIDAD',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=290)
        peso=Label(ventana2,text='800KG',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=320)
        baterias=Label(ventana2,text='4',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=350)
        tension=Label(ventana2,text='0,60V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=380)
        eficiencia=Label(ventana2,text='8',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=410)
        temporada=Label(ventana2,text='2019',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=440)
        ppB=Label(ventana2,text='3',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=470)
        
        
        ventana2.mainloop()
        
    def ventana3():

        ventana3=Toplevel()
        ventana3.config(width=500,height=500,bg="black")
        icono=ventana3.iconbitmap('f1logo.ico')
        ventana3.resizable(width=False,height=False)
        pistaIma=PhotoImage(file='pista.png')
        pista=Label(ventana3,image=pistaIma).place(x=0,y=0)
        vehiculo3=PhotoImage(file='auto3.png')
        carro3=Label(ventana3,image=vehiculo3)
        carro3.place(x=0,y=0)
        nombre=Label(ventana3,text='nombre:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=140)
        pais=Label(ventana3,text='Pais:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=170)
        modelo=Label(ventana3,text='Modelo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=200)
        estado=Label(ventana3,text='Estado:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=230)
        consumo=Label(ventana3,text='Consumo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=260)
        sensores=Label(ventana3,text='Sensores:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=290)
        peso=Label(ventana3,text='Peso:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=320)
        baterias=Label(ventana3,text='baterias:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=350)
        tension=Label(ventana3,text='tension:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=380)
        eficiencia=Label(ventana3,text='Eficiencia:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=410)
        temporada=Label(ventana3,text='Temporada:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=440)
        ppB=Label(ventana3,text='PPB:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=470)
        ## RESPUESTA ##
        nombre=Label(ventana3,text='HONDA RA619H9:',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=140)
        pais=Label(ventana3,text='FRANCIA',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=170)
        modelo=Label(ventana3,text='2010',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=200)
        estado=Label(ventana3,text='DISPONIBLE',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=230)
        consumo=Label(ventana3,text='2,0V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=260)
        sensores=Label(ventana3,text='LUZ',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=290)
        peso=Label(ventana3,text='780KG',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=320)
        baterias=Label(ventana3,text='4',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=350)
        tension=Label(ventana3,text='0,70V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=380)
        eficiencia=Label(ventana3,text='10',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=410)
        temporada=Label(ventana3,text='2018',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=440)
        ppB=Label(ventana3,text='4',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=470)
        
        ventana3.mainloop()
    def ventana4():

        ventana4=Toplevel()
        ventana4.config(width=500,height=500,bg="black")
        icono=ventana4.iconbitmap('f1logo.ico')
        ventana4.resizable(width=False,height=False)
        pistaIma=PhotoImage(file='pista.png')
        pista=Label(ventana4,image=pistaIma).place(x=0,y=0)
        vehiculo4=PhotoImage(file='auto4.png')
        carro4=Label(ventana4,image=vehiculo4)
        carro4.place(x=0,y=0)
        nombre=Label(ventana4,text='nombre:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=140)
        pais=Label(ventana4,text='Pais:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=170)
        modelo=Label(ventana4,text='Modelo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=200)
        estado=Label(ventana4,text='Estado:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=230)
        consumo=Label(ventana4,text='Consumo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=260)
        sensores=Label(ventana4,text='Sensores:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=290)
        peso=Label(ventana4,text='Peso:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=320)
        baterias=Label(ventana4,text='baterias:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=350)
        tension=Label(ventana4,text='tension:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=380)
        eficiencia=Label(ventana4,text='Eficiencia:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=410)
        temporada=Label(ventana4,text='Temporada:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=440)
        ppB=Label(ventana4,text='PPB:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=470)
        ### RESPUESTA  ###
        nombre=Label(ventana4,text='RENAULT E-TECH 19:',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=140)
        pais=Label(ventana4,text='ITALIA',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=170)
        modelo=Label(ventana4,text='2018',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=200)
        estado=Label(ventana4,text='DISPONIBLE',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=230)
        consumo=Label(ventana4,text='1,70V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=260)
        sensores=Label(ventana4,text='LUZ-PROXIMIDAD',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=290)
        peso=Label(ventana4,text='760KG',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=320)
        baterias=Label(ventana4,text='4',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=350)
        tension=Label(ventana4,text='0,49V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=380)
        eficiencia=Label(ventana4,text='9',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=410)
        temporada=Label(ventana4,text='2019',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=440)
        ppB=Label(ventana4,text='4',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=470)
        
        
        ventana4.mainloop()

        
    def ventana5():
        ventana5=Toplevel()
        ventana5.config(width=500,height=500,bg="black")
        icono=ventana5.iconbitmap('f1logo.ico')
        ventana5.resizable(width=False,height=False)
        pistaIma=PhotoImage(file='pista.png')
        pista=Label(ventana5,image=pistaIma).place(x=0,y=0)
        vehiculo5=PhotoImage(file='auto5.png')
        carro5=Label(ventana5,image=vehiculo5)
        carro5.place(x=0,y=0)
        nombre=Label(ventana5,text='nombre:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=140)
        pais=Label(ventana5,text='Pais:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=170)
        modelo=Label(ventana5,text='Modelo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=200)
        estado=Label(ventana5,text='Estado:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=230)
        consumo=Label(ventana5,text='Consumo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=260)
        sensores=Label(ventana5,text='Sensores:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=290)
        peso=Label(ventana5,text='Peso:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=320)
        baterias=Label(ventana5,text='baterias:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=350)
        tension=Label(ventana5,text='tension:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=380)
        eficiencia=Label(ventana5,text='Eficiencia:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=410)
        temporada=Label(ventana5,text='Temporada:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=440)
        ppB=Label(ventana5,text='PPB:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=470)
        ### RESPUESTA  ###
        nombre=Label(ventana5,text='FERRARI 06413:',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=140)
        pais=Label(ventana5,text='ESCOCIA',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=170)
        modelo=Label(ventana5,text='2019',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=200)
        estado=Label(ventana5,text='AGOTADO',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=230)
        consumo=Label(ventana5,text='1,70V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=260)
        sensores=Label(ventana5,text='LUZ',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=290)
        peso=Label(ventana5,text='780KG',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=320)
        baterias=Label(ventana5,text='4',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=350)
        tension=Label(ventana5,text='0,49V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=380)
        eficiencia=Label(ventana5,text='9',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=410)
        temporada=Label(ventana5,text='2017',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=440)
        ppB=Label(ventana5,text='4',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=470)
        
        ventana5.mainloop()

         
    def ventana6():
        ventana6=Toplevel()
        ventana6.config(width=500,height=500,bg="black")
        icono=ventana6.iconbitmap('f1logo.ico')
        ventana6.resizable(width=False,height=False)
        pistaIma=PhotoImage(file='pista.png')
        pista=Label(ventana6,image=pistaIma).place(x=0,y=0)
        vehiculo6=PhotoImage(file='auto6.png')
        carro6=Label(ventana6,image=vehiculo6)
        carro6.place(x=0,y=0)
        nombre=Label(ventana6,text='nombre:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=140)
        pais=Label(ventana6,text='Pais:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=170)
        modelo=Label(ventana6,text='Modelo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=200)
        estado=Label(ventana6,text='Estado:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=230)
        consumo=Label(ventana6,text='Consumo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=260)
        sensores=Label(ventana6,text='Sensores:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=290)
        peso=Label(ventana6,text='Peso:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=320)
        baterias=Label(ventana6,text='baterias:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=350)
        tension=Label(ventana6,text='tension:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=380)
        eficiencia=Label(ventana6,text='Eficiencia:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=410)
        temporada=Label(ventana6,text='Temporada:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=440)
        ppB=Label(ventana6,text='PPB:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=470)
        ### RESPUESTA  ###
        nombre=Label(ventana6,text='RENAULT E-TECH 1916:',bd=4,bg="black",fg="white").place(x=300,y=140)
        pais=Label(ventana6,text='PORTUGAL',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=170)
        modelo=Label(ventana6,text='2019',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=200)
        estado=Label(ventana6,text='AGOTADO',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=230)
        consumo=Label(ventana6,text='2,40V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=260)
        sensores=Label(ventana6,text='LUZ',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=290)
        peso=Label(ventana6,text='750KG',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=320)
        baterias=Label(ventana6,text='3',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=350)
        tension=Label(ventana6,text='0,50V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=380)
        eficiencia=Label(ventana6,text='7',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=410)
        temporada=Label(ventana6,text='2019',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=440)
        ppB=Label(ventana6,text='8',bd=4,bg="black",fg="white").place(x=300,y=470)
        
        
        ventana6.mainloop()
        
    def ventana7():
        ventana7=Toplevel()
        ventana7.config(width=500,height=500,bg="black")
        icono=ventana7.iconbitmap('f1logo.ico')
        ventana7.resizable(width=False,height=False)
        pistaIma=PhotoImage(file='pista.png')
        pista=Label(ventana7,image=pistaIma).place(x=0,y=0)
        vehiculo7=PhotoImage(file='auto7.png')
        carro7=Label(ventana7,image=vehiculo7)
        carro7.place(x=0,y=0)
        nombre=Label(ventana7,text='nombre:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=140)
        pais=Label(ventana7,text='Pais:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=170)
        modelo=Label(ventana7,text='Modelo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=200)
        estado=Label(ventana7,text='Estado:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=230)
        consumo=Label(ventana7,text='Consumo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=260)
        sensores=Label(ventana7,text='Sensores:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=290)
        peso=Label(ventana7,text='Peso:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=320)
        baterias=Label(ventana7,text='baterias:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=350)
        tension=Label(ventana7,text='tension:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=380)
        eficiencia=Label(ventana7,text='Eficiencia:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=410)
        temporada=Label(ventana7,text='Temporada:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=440)
        ppB=Label(ventana7,text='PPB:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=470)
        ### RESPUESTA  ###
        nombre=Label(ventana7,text='BWT MERCEDES-AMG F1:',bd=4,bg="black",fg="white").place(x=300,y=140)
        pais=Label(ventana7,text='POLONIA',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=170)
        modelo=Label(ventana7,text='2013',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=200)
        estado=Label(ventana7,text='AGOTADO',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=230)
        consumo=Label(ventana7,text='1,40V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=260)
        sensores=Label(ventana7,text='LUZ-PROXIMIDAD',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=290)
        peso=Label(ventana7,text='720KG',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=320)
        baterias=Label(ventana7,text='4',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=350)
        tension=Label(ventana7,text='0,49V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=380)
        eficiencia=Label(ventana7,text='9',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=410)
        temporada=Label(ventana7,text='2019',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=440)
        ppB=Label(ventana7,text='3',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=470)
        
        
        
        ventana7.mainloop()
        
    def ventana8():
        ventana8=Toplevel()
        ventana8.config(width=500,height=500,bg="black")
        icono=ventana8.iconbitmap('f1logo.ico')
        ventana8.resizable(width=False,height=False)
        pistaIma=PhotoImage(file='pista.png')
        pista=Label(ventana8,image=pistaIma).place(x=0,y=0)
        vehiculo8=PhotoImage(file='auto8.png')
        carro8=Label(ventana8,image=vehiculo8)
        carro8.place(x=0,y=0)
        nombre=Label(ventana8,text='nombre:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=140)
        pais=Label(ventana8,text='Pais:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=170)
        modelo=Label(ventana8,text='Modelo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=200)
        estado=Label(ventana8,text='Estado:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=230)
        consumo=Label(ventana8,text='Consumo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=260)
        sensores=Label(ventana8,text='Sensores:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=290)
        peso=Label(ventana8,text='Peso:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=320)
        baterias=Label(ventana8,text='baterias:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=350)
        tension=Label(ventana8,text='tension:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=380)
        eficiencia=Label(ventana8,text='Eficiencia:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=410)
        temporada=Label(ventana8,text='Temporada:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=440)
        ppB=Label(ventana8,text='PPB:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=470)
        ### RESPUESTA  ###
        nombre=Label(ventana8,text='FERRARI 06426:',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=140)
        pais=Label(ventana8,text='INGLATERRA',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=170)
        modelo=Label(ventana8,text='2018',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=200)
        estado=Label(ventana8,text='AGOTADO',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=230)
        consumo=Label(ventana8,text='1,40V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=260)
        sensores=Label(ventana8,text='LUZ',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=290)
        peso=Label(ventana8,text='730KG',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=320)
        baterias=Label(ventana8,text='4',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=350)
        tension=Label(ventana8,text='0,49V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=380)
        eficiencia=Label(ventana8,text='7',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=410)
        temporada=Label(ventana8,text='2019',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=440)
        ppB=Label(ventana8,text='6',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=470)
        
        
        
        ventana8.mainloop()
        
    def ventana9():

        ventana9=Toplevel()
        ventana9.config(width=500,height=500,bg="black")
        icono=ventana9.iconbitmap('f1logo.ico')
        ventana9.resizable(width=False,height=False)
        pistaIma=PhotoImage(file='pista.png')
        pista=Label(ventana9,image=pistaIma).place(x=0,y=0)
        vehiculo9=PhotoImage(file='auto9.png')
        carro9=Label(ventana9,image=vehiculo9)
        carro9.place(x=0,y=0)
        nombre=Label(ventana9,text='nombre:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=140)
        pais=Label(ventana9,text='Pais:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=170)
        modelo=Label(ventana9,text='Modelo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=200)
        estado=Label(ventana9,text='Estado:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=230)
        consumo=Label(ventana9,text='Consumo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=260)
        sensores=Label(ventana9,text='Sensores:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=290)
        peso=Label(ventana9,text='Peso:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=320)
        baterias=Label(ventana9,text='baterias:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=350)
        tension=Label(ventana9,text='tension:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=380)
        eficiencia=Label(ventana9,text='Eficiencia:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=410)
        temporada=Label(ventana9,text='Temporada:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=440)
        ppB=Label(ventana9,text='PPB:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=470)
        ### RESPUESTA  ###
        nombre=Label(ventana9,text='HONDA RA619H28:',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=140)
        pais=Label(ventana9,text='HOLANDA',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=170)
        modelo=Label(ventana9,text='2016',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=200)
        estado=Label(ventana9,text='DISPONIBLE',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=230)
        consumo=Label(ventana9,text='Consumo',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=260)
        sensores=Label(ventana9,text='LUZ-PROXIMIDAD',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=290)
        peso=Label(ventana9,text='790KG',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=320)
        baterias=Label(ventana9,text='3',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=350)
        tension=Label(ventana9,text='0,40V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=380)
        eficiencia=Label(ventana9,text='9',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=410)
        temporada=Label(ventana9,text='2010',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=440)
        ppB=Label(ventana9,text='4:',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=470)
        
        
        ventana9.mainloop()
    def ventana10():

        ventana10=Toplevel()
        ventana10.config(width=500,height=500,bg="black")
        icono=ventana10.iconbitmap('f1logo.ico')
        ventana10.resizable(width=False,height=False)
        pistaIma=PhotoImage(file='pista.png')
        pista=Label(ventana10,image=pistaIma).place(x=0,y=0)
        vehiculo10=PhotoImage(file='auto10.png')
        carro10=Label(ventana10,image=vehiculo10)
        carro10.place(x=0,y=0)
        nombre=Label(ventana10,text='nombre:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=140)
        pais=Label(ventana10,text='Pais:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=170)
        modelo=Label(ventana10,text='Modelo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=200)
        estado=Label(ventana10,text='Estado:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=230)
        consumo=Label(ventana10,text='Consumo:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=260)
        sensores=Label(ventana10,text='Sensores:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=290)
        peso=Label(ventana10,text='Peso:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=320)
        baterias=Label(ventana10,text='baterias:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=350)
        tension=Label(ventana10,text='tension:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=380)
        eficiencia=Label(ventana10,text='Eficiencia:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=410)
        temporada=Label(ventana10,text='Temporada:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=440)
        ppB=Label(ventana10,text='PPB:',bd=4,bg="black",fg="white",width=15 ).place(x=10,y=470)
        ### RESPUESTA  ###
        nombre=Label(ventana10,text='MERCEDES-AMG F1 M10 EQ:',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=140)
        pais=Label(ventana10,text='MEXICO',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=170)
        modelo=Label(ventana10,text='2015',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=200)
        estado=Label(ventana10,text='DISPONIBLE',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=230)
        consumo=Label(ventana10,text='1,40V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=260)
        sensores=Label(ventana10,text='LUZ-VELOCIDAD',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=290)
        peso=Label(ventana10,text='755KG',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=320)
        baterias=Label(ventana10,text='2',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=350)
        tension=Label(ventana10,text='0,50V',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=380)
        eficiencia=Label(ventana10,text='8',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=410)
        temporada=Label(ventana10,text='2019',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=440)
        ppB=Label(ventana10,text='4',bd=4,bg="black",fg="white",width=15 ).place(x=300,y=470)
        
        
        ventana10.mainloop()


    def revisar(x):
        if x==1:
            return ventana1()
        if x==2:
            return ventana2()
        if x==3:
            return ventana3()
        if x==4:
            return ventana4()
        if x==5:
            return ventana5()
        if x==6:
            return ventana6()
        if x==7:
            return ventana7()
        if x==8:
            return ventana8()
        if x==9:
            return ventana9()
        if x==10:
            return ventana10()

    vehiculos.mainloop()

ventana_principal()

 
        
  
  










