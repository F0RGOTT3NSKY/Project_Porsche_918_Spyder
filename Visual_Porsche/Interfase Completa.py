from tkinter import *
import tkinter
import random

global msj,msj1,msj2,msj3
msj = "Red Bull.png"
msj1 = "Red Bull.png"
msj2 = "Red Bull.png"
msj3 = "LOGO.png"

def ventana_inicio():
    global window,root,datos,msj,msj1,msj2
    window = Tk()
    window.title('Proyecto III')
    window.minsize(700,700)
    window.resizable(width = NO,height = NO)

    def fileR():
        file=open("Pilotos.txt","r")
        texto=file.read()
        datos=eval(texto)
        file.close()
        return datos

    #Canvas para los botones y el texto
    C_w = Canvas(window, width = 700, height = 700)
    C_w.place(x = 0,y = 0)

    scrollbar = Scrollbar(C_w)
    scrollbar.place(x = 135, y = 480)

    Lista = fileR()
    
    mylist = Listbox(C_w, yscrollcommand = scrollbar.set)
    
    for line in range(0,len(Lista[0])):
        disponible = random.randint(0,1)
        if(disponible == 1):
            mylist.insert(END, Lista[0][line][0])
        else:
            pass

    mylist.place(x = 10, y = 480)
    scrollbar.config(command = mylist.yview)

    scrollbaraut = Scrollbar(C_w)
    scrollbaraut.place(x = 385, y = 480)

    carros = Listbox(C_w, yscrollcommand = scrollbar.set)
    
    for line in range(len(Lista[1])):
        disponible = random.randint(0,1)
        if(disponible == 1):
            carros.insert(END, Lista[1][line][0])
        else:
            pass

    carros.place(x = 260, y = 480)
    scrollbaraut.config(command = carros.yview)


    #Botones
    B_Pos = Button(C_w,text = 'Tabla de posicionamientos',command=lambda: Tabla(),fg='white', bg = 'black', font = ('Arial',12))
    B_Pos.place(x = 495,y = 555)

    B_Test = Button(C_w,text = 'Test Drive',fg='white', bg = 'black', font = ('Arial',12))
    B_Test.place(x = 612,y = 590)

    B_Pat = Button(C_w,text = 'Editar',fg='white',command=lambda:editar(), bg = 'black', font = ('Arial',12))
    B_Pat.place(x = 641,y = 625)

    B_About = Button(C_w,text = 'About',command=lambda: ventana_about(),fg='white', bg = 'black', font = ('Arial',12))
    B_About.place(x = 642,y = 660)

    #Texto
    L_Nombre = Label(C_w, text = 'Nombre de Escudería', font = ('Verdana',14, "bold"),fg = 'black')
    L_Nombre.place(x = 5,y =5)

    L_Logo = Label(C_w, text = 'EscudeTEC', font = ('Arial',14),fg = 'black')
    L_Logo.place(x = 150,y = 45)

    L_UG = Label(C_w, text = 'Ubicación:\n', font = ('Verdana',14, "bold"),fg = 'black')
    L_UG.place(x = 5,y =85)

    L_Logo = Label(C_w, text = 'Costa Rica', font = ('Arial',14),fg = 'black')
    L_Logo.place(x = 150,y = 125)

    L_Pat = Label(C_w, text = 'Patrocinadores:', font = ('Verdana',14, "bold"),fg = 'black')
    L_Pat.place(x = 5,y =165)

    L_Pilotos = Label(C_w, text = 'Pilotos disponibles:', font = ('Verdana',14, "bold"),fg = 'black')
    L_Pilotos.place(x = 5,y =425)

    L_Aut = Label(C_w, text = 'Participaciones con:', font = ('Verdana',14, "bold"),fg = 'black')
    L_Aut.place(x = 250,y =425)

    pat=PhotoImage(file=msj)
    patr=Label(C_w,image=pat,width=150,height=150).place(x=25,y=225)

    pat1=PhotoImage(file=msj1)
    patr1=Label(C_w,image=pat1,width=150,height=150).place(x=225,y=225)

    pat2=PhotoImage(file=msj2)
    patr2=Label(C_w,image=pat2,width=150,height=150).place(x=425,y=225)

    LOGO=PhotoImage(file=msj3)
    LOGO1=Label(C_w,image=LOGO,width=200,height=200).place(x=500,y=0)

    window.mainloop()
    

def ventana_about():
    global window,root
    window.destroy()

    root =  Tk()
    root.minsize(700,700)
    root.title('About')
    root.resizable(width = NO,height = NO)
    boton = tkinter.Button(root, text="Volver a la Página principal",command=lambda: about_inicio())
    boton.place(x=270,y=650)
    a=Label(root, text=("Créditos "),justify=LEFT, font=("Verdana", 20, "bold"))
    a.place(x=300,y=25)
    b=Label(root, text=("Institución: Instituto Tecnológico de Costa Rica "),justify=LEFT, font=("Arial", 15, "bold"))
    b.place(x=30,y=75)
    c=Label(root, text=("Autores:"),justify=LEFT, font=("Arial", 15, "bold"))
    c.place(x=30,y=125)
    d=Label(root, text=("Leonardo Guillén Fernandez     2019031688"),justify=LEFT, font=("Arial", 15, "bold"))
    d.place(x=60,y=150)
    img=PhotoImage(file='leo.gif')
    logo1=Label(root,image=img,width=150,height=200).place(x=525,y=75)
    e=Label(root, text=("Marco Rivera Serrano               2018118206"),justify=LEFT, font=("Arial", 15, "bold"))
    e.place(x=60,y=225)
    img5=PhotoImage(file='marco.gif')
    
    logo5=Label(root,image=img5,width=150,height=200).place(x=525,y=350)
    f=Label(root, text=("Carrera: Ingeniería en Computadores"),justify=LEFT, font=("Arial", 15, "bold"))
    f.place(x=30,y=300)
    g=Label(root, text=("Curso: Taller de Programación"),justify=LEFT, font=("Arial", 15, "bold"))
    g.place(x=30,y=350)
    h=Label(root, text=("Grupo:1"),justify=LEFT, font=("Arial", 15, "bold"))
    h.place(x=30,y=400)
    i=Label(root, text=("Versión: 1.0  Costa Rica   Año:2019"),justify=LEFT, font=("Arial", 15, "bold"))
    i.place(x=30,y=450)
    j=Label(root, text=("Profesor: Pedro Gutierrez"),justify=LEFT, font=("Arial", 15, "bold"))
    j.place(x=30,y=500)
    root.mainloop()

def about_inicio():
    root.destroy()
    ventana_inicio()

def Tabla():
    global window,tabla,datos
    def fileR():
        file=open("Pilotos.txt","r")
        texto=file.read()
        datos=eval(texto)
        file.close()
        return datos

    def flecha(datos,i,j):
        global label
        if(i == 5):
            fileW(datos)
            return crear()
        else:
            temp = datos[0][i]
            datos[0][i] = datos[0][j]
            datos[0][j] = temp
            return flecha(datos,i+1,j-1)
        
    def fileW(com):
        newfile=open("Pilotos.txt","w")
        newfile.write(str(com))
        newfile.close()
        return com

    def carro(i):
        Lista = fileR()
        Lista = Lista[0]
        Carros = fileR()
        Carros = Carros[1]
        CAR = Lista[i][9]
        línea = 0
        while línea != len(Carros):
            if(CAR == Carros[línea][0]):
                return infocar(Carros,línea)
            else:
                línea +=1

    def infocar(Carros,i):
        info = Toplevel()
        info.minsize(700,300)
        info.resizable(width = NO,height = NO)

        #LABELS DE CABECERA

        N_Car = Label(info, text = "Nombre:", font = ('Arial',11)).place(x = 0,y = 0)
        M_Car = Label(info, text = "Modelo:", font = ('Arial',11)).place(x = 0,y = 25)
        P_Car = Label(info, text = "País:", font = ('Arial',11)).place(x = 0,y = 50)
        E_Car = Label(info, text = "Estado:", font = ('Arial',11)).place(x = 0,y = 75)
        C_Car = Label(info, text = "Consumo:", font = ('Arial',11)).place(x = 0,y = 100)
        S_Car = Label(info, text = "Sensores:", font = ('Arial',11)).place(x = 0,y = 125)
        Pe_Car = Label(info, text = "Peso(Kg):", font = ('Arial',11)).place(x = 0,y = 150)
        Efi_Car = Label(info, text = "Eficiencia:", font = ('Arial',11)).place(x = 0,y = 175)
        Se_Car = Label(info, text = "Temporada:", font = ('Arial',11)).place(x = 0,y = 200)
        B_Car = Label(info, text = "Baterías:", font = ('Arial',11)).place(x = 0,y = 225)
        P_B_Car = Label(info, text = "PpB:", font = ('Arial',11)).place(x = 0,y = 250)
        T_B_Car = Label(info, text = "Tensión:", font = ('Arial',11)).place(x = 0,y = 275)
        
        #LA INFO DE CADA CARRO
        Nombre = Label(info, text = Carros[i][0], font = ('Arial',11)).place(x = 100,y = 0)
        Modelo = Label(info, text = Carros[i][1], font = ('Arial',11)).place(x = 100,y = 25)
        País = Label(info, text = Carros[i][2], font = ('Arial',11)).place(x = 100,y = 50)

        F_CAR=PhotoImage(file=Carros[i][3])
        F_CARr=Label(info,image=F_CAR,width=200,height=100).place(x=500,y=0)
        
        Estado = Label(info, text = Carros[i][4], font = ('Arial',11)).place(x = 100,y = 75)
        Consumo = Label(info, text = Carros[i][5], font = ('Arial',11)).place(x = 100,y = 100)
        Sensores = Label(info, text = Carros[i][6], font = ('Arial',11)).place(x = 100,y = 125)
        peso = Label(info, text = Carros[i][7], font = ('Arial',11)).place(x = 100,y = 150)
        Eficiencia = Label(info, text = Carros[i][8], font = ('Arial',11)).place(x = 100,y = 175)
        Season = Label(info, text = Carros[i][9], font = ('Arial',11)).place(x = 100,y = 200)
        Baterías = Label(info, text = Carros[i][10], font = ('Arial',11)).place(x = 100,y = 225)
        P_baterías = Label(info, text = Carros[i][11], font = ('Arial',11)).place(x = 100,y = 250)
        T_Baterías = Label(info, text = Carros[i][12], font = ('Arial',11)).place(x = 100,y = 275)    

        info.mainloop()

    window.destroy()
    tabla = Tk()
    tabla.minsize(900,290)
    tabla.resizable(width = NO,height = NO)
    root = Canvas(tabla, width = 700, height = 700)
    root.place(x = 0, y = 0)

    back = Button(tabla, text = 'Volver a la página principal', command = lambda:tabla_inicio(), font = ('Arial', 15))
    back.place(relx=0.5, rely=0.92, anchor=CENTER)

    button = Button(tabla, text = 'Carro',command = lambda:carro(0), font = ('Arial', 6)).place(x = 780, y = 30)
    
    button1 = Button(tabla, text = 'Carro',command = lambda:carro(1), font = ('Arial', 6)).place(x = 780, y = 51)

    button2 = Button(tabla, text = 'Carro',command = lambda:carro(2), font = ('Arial', 6)).place(x = 780, y = 72)

    button3 = Button(tabla, text = 'Carro',command = lambda:carro(3), font = ('Arial', 6)).place(x = 780, y = 93)

    button4 = Button(tabla, text = 'Carro',command = lambda:carro(4), font = ('Arial', 6)).place(x = 780, y = 114)

    button5 = Button(tabla, text = 'Carro',command = lambda:carro(5), font = ('Arial', 6)).place(x = 780, y = 135)

    button6 = Button(tabla, text = 'Carro',command = lambda:carro(6), font = ('Arial', 6)).place(x = 780, y = 156)

    button7 = Button(tabla, text = 'Carro',command = lambda:carro(7), font = ('Arial', 6)).place(x = 780, y = 177)

    button8 = Button(tabla, text = 'Carro',command = lambda:carro(8), font = ('Arial', 6)).place(x = 780, y = 198)

    button9 = Button(tabla, text = 'Carro',command = lambda:carro(9), font = ('Arial', 6)).place(x = 780, y = 219)

    label_1 = Label(root, text = "Nombre", bg = 'deep sky blue', font = ('Arial',11)).grid(row = 0)
    label_2 = Label(root, text = "Edad", bg = 'lawn green', font = ('Arial',11)).grid(row = 0, column = 1)
    label_3 = Label(root, text = "Nacionalidad", bg = 'sandy brown', font = ('Arial',11)).grid(row = 0, column = 2)
    label_4 = Label(root, text = "Temporada", bg = 'lavender', font = ('Arial',11)).grid(row = 0, column = 3)
    label_5 = Label(root, text = "Participaciones", bg = 'light slate blue', font = ('Arial',11)).grid(row = 0, column = 4)
    label_6 = Label(root, text = "Destacadas", bg = 'orange red', font = ('Arial',11)).grid(row = 0, column = 5)
    label_7 = Label(root, text = "Cant. en podio", bg = 'aquamarine', font = ('Arial',11)).grid(row = 0, column = 6)
    label_8 = Label(root, text = "Movimiento", bg = 'olive drab', font = ('Arial',11)).grid(row = 0, column = 7)
    label_9 = Label(root, text = "Score", bg = 'orange', font = ('Arial',11)).grid(row = 0, column = 8)
    orden = Button(root, text = '↕', font = ('Arial', 11), command=lambda:flecha(datos,0,9)).grid(row = 0, column = 10)

    def crear():
        global datos
        datos = fileR()

        pilotos = 0
        categoría = 1

        for pilotos in range(0,10):
            for categoría in range(0,9):
                global label
                label = StringVar()
                Label(root, textvariable = label).grid(row = pilotos + 1, column = categoría, sticky=W)
                label.set(datos[0][pilotos][categoría])

    crear()

    tabla.mainloop()

def tabla_inicio():
    tabla.destroy()
    ventana_inicio()

def editar():
    global window,edit

    def fileR():
        file=open("Pilotos.txt","r")
        texto=file.read()
        datos=eval(texto)
        file.close()
        return datos

    def entries(i):
        global msj,msj1,msj2,msj3
        msj = str(e1.get())

        INFO = fileR()
        INFO = INFO[2]
        if(i==len(INFO)):
            return print("Revise la información introducida del patrocinador 1")
        if(INFO[i] == msj):
            return entries1(0)
        else:
            return entries(i+1)

    def entries1(i):
        global msj,msj1,msj2,msj3
        msj1 = str(e2.get())

        INFO = fileR()
        INFO = INFO[2]
        if(i==len(INFO)):
            return print("Revise la información introducida del patrocinador 2")
        if(INFO[i] == msj1):
            return entries2(0)
        else:
            return entries1(i+1)
            
    def entries2(i):
        global msj,msj1,msj2,msj3
        msj2 = str(e3.get())
        INFO = fileR()
        INFO = INFO[2]
        if(i==len(INFO)):
            return print("Revise la información introducida  del patrocinador 3")
        if(INFO[i] == msj2):
            return entries3(0)
        else:
            return entries2(i+1)

    def entries3(i):
        global msj,msj1,msj2,msj3
        msj3 = str(e4.get())
        INFO = fileR()
        INFO = INFO[3]
        if(i==len(INFO)):
            return print("Revise la información introducida del logo")
        if(INFO[i] == msj3):
            return edit_inicio()
        else:
            return entries3(i+1)
    
    window.destroy()
    edit = Tk()
    edit.title("Proyecto III")
    edit.minsize(300,320)
    edit.resizable(width = NO,height = NO)

    Label(edit, text="Patrocinador 1").grid(row=0, column = 0, sticky=W)
    Label(edit, text="Patrocinador 2").grid(row=0, column = 2, sticky=W)
    Label(edit, text="Patrocinador 3").grid(row=0, column = 4, sticky=W)
    Label(edit, text="Logo").grid(row=1, sticky=W)

    e1 = Entry(edit)
    e2 = Entry(edit)
    e3 = Entry(edit)
    e4 = Entry(edit)

    e1.grid(row = 0, column = 1)
    e2.grid(row = 0, column = 3)
    e3.grid(row = 0, column = 5)
    e4.grid(row=1, column=1)

    patrocinadores = Scrollbar(edit)
    patrocinadores.place(x = 128, y = 70)

    mylist = Listbox(edit, yscrollcommand = patrocinadores.set)

    lista = fileR()

    for i in range(0,len(lista[2])):
        mylist.insert(END,lista[2][i])

    mylist.place(x = 5, y = 70)
    patrocinadores.config(command = mylist.yview)

    #LOGO################################################

    Logo = Scrollbar(edit)
    Logo.place(x = 323, y = 70)

    mylist = Listbox(edit, yscrollcommand = Logo.set)

    lista = fileR()

    for i in range(0,len(lista[3])):
        mylist.insert(END,lista[3][i])

    mylist.place(x = 200, y = 70)
    Logo.config(command = mylist.yview)

    B_Save = Button(edit,text = 'Guardar Cambios',fg='white', command=lambda:entries(0),bg = 'black', font = ('Arial',12))
    B_Save.place(x = 5,y = 240)

    B_Cancelar = Button(edit,text = 'Cancelar',command=lambda:edit_inicio(),fg='white', bg = 'black', font = ('Arial',12))
    B_Cancelar.place(x = 5,y = 280)

    B_Pilotos = Button(edit,text = 'Editar pilotos',command=lambda:edit_pilotos(),fg='white', bg = 'black', font = ('Arial',12))
    B_Pilotos.place(x = 510,y = 280)

    Label(edit, text = 'Ingrese el texto junto con la \n extención .png', font = ('Arial',14),fg = 'red').place(x=350, y = 60)
    Label(edit, text = 'Patrocinadores:', font = ('Arial',10),fg = 'black').place(x=0, y = 45)
    Label(edit, text = 'Logos:', font = ('Arial',10),fg = 'black').place(x=197, y = 45)

def edit_inicio():
    edit.destroy()
    ventana_inicio()

def edit_pilotos():
    global edit,pilotos

    def edit_pilotos_inicio():
        pilotos.destroy()
        ventana_inicio()

    def fileR():
        file=open("Pilotos.txt","r")
        texto=file.read()
        datos=eval(texto)
        file.close()
        return datos

    def orden():
        i=0
        lista1 = fileR()
        lista2 = lista1[0]
        return sel_Aux(lista2,0,1)

    def Buscar():
        Conductor = str(ep.get())
        if(len(Conductor)==0):
            return print("Ingrese un nombre")
        else:
            pass
        
        Lista = fileR()
        Lista = Lista[0]
        for i in range(len(Lista)):
            if(Conductor == Lista[i][0]):
                return Buscar_aux(i)
            else:
                pass

        print(Conductor,"no está en la base de datos")


    
    edit.destroy()
    pilotos = Tk()
    pilotos.title("Proyecto III")
    pilotos.minsize(350,100)
    pilotos.resizable(width = NO,height = NO)

    Label(pilotos, text = 'Ingrese el piloto a editar', font = ('Arial',12),fg = 'black').grid(row = 0,column = 0)
    ep = Entry(pilotos)
    ep.grid(row = 0,column = 1)

    B_Buscar = Button(pilotos,text = 'Buscar',command=lambda:Buscar(),fg='white',bg = 'black', font = ('Arial',12))
    B_Buscar.place(x = 5,y = 30)

    B_Cancelar = Button(pilotos,text = 'Cancelar',command=lambda:edit_pilotos_inicio(),fg='white', bg = 'black', font = ('Arial',12))
    B_Cancelar.place(x = 5,y = 65)
    
def Buscar_aux(i):
    global pilotos,P_INFO

    def Buscar_inicio():
        P_INFO.destroy()
        ventana_inicio()

    def fileR():
        file=open("Pilotos.txt","r")
        texto=file.read()
        datos=eval(texto)
        file.close()
        return datos
    
    def orden():
        i=0
        lista1 = fileR()
        lista2 = lista1[0]
        return sel_aux(lista2,0,1)

    def sel_aux(lista,indice_i,indice_m):
        if(indice_i == len(lista)-1):
            return Buscar_inicio()
        else:
            primero = lista[indice_i]
            Min = menor(lista[indice_m:],0,lista[indice_m][8],0)
            Min = Min + indice_m
            if(primero[8]>lista[Min][8]):
                
                temp = primero
                lista[indice_i] = lista[Min]
                lista[Min] = temp
                return sel_aux(lista,indice_i+1,indice_m+1)
            else:
                return sel_aux(lista,indice_i+1,indice_m+1)

    def menor(lista,indice,men,posmen):
        if(indice == len(lista)):
            return posmen
        else:
            if(men>lista[indice][8]):
                men = lista[indice][8]
                posmen = indice
                return menor(lista,indice+1,men,posmen)
            else:
                return menor(lista,indice+1,men,posmen)

    def Cambios(Lista):
        me1 = str(e1.get())
        me2 = str(e2.get())
        me3 = str(e3.get())
        me4 = str(e4.get())
        me5 = str(e5.get())
        me6 = str(e6.get())
        if(len(me1)==0 or len(me2)==0 or len(me3)==0 or len(me4)==0 or len(me5)==0 or len(me6)==0):
            return print("Ingrese datos en todas las casillas")
        else:
            Lista[0][i][0] = me1
            Lista[0][i][1] = me2
            Lista[0][i][2] = me3
            Lista[0][i][4] = me4
            Lista[0][i][5] = me5
            Lista[0][i][6] = me6
            fileW(Lista)
            return orden()
            
    def fileW(com):
        newfile=open("Pilotos.txt","w")
        newfile.write(str(com))
        newfile.close()
        return com
        

    Lista = fileR()
        
    pilotos.destroy()
    P_INFO = Tk()
    P_INFO.title("Proyecto III")
    P_INFO.minsize(350,320)
    P_INFO.resizable(width = NO,height = NO)

    Label(P_INFO, text = "Nombre:", font = ('Arial',9),fg = 'black').grid(row = 0,column = 0, sticky = W)
    Label(P_INFO, text = "Edad:", font = ('Arial',9),fg = 'black').grid(row = 0,column = 1, sticky = W)
    Label(P_INFO, text = "País", font = ('Arial',9),fg = 'black').grid(row = 0,column = 2, sticky = W)
    Label(P_INFO, text = "Entradas", font = ('Arial',9),fg = 'black').grid(row = 0,column = 3, sticky = W)
    Label(P_INFO, text = "Victorias", font = ('Arial',9),fg = 'black').grid(row = 0,column = 4, sticky = W)
    Label(P_INFO, text = "Podio", font = ('Arial',9),fg = 'black').grid(row = 0,column = 5, sticky = W)

    Label(P_INFO, text = Lista[0][i][0], font = ('Arial',9),fg = 'black').grid(row = 1,column = 0, sticky = W)
    Label(P_INFO, text = Lista[0][i][1], font = ('Arial',9),fg = 'black').grid(row = 1,column = 1, sticky = W)
    Label(P_INFO, text = Lista[0][i][2], font = ('Arial',9),fg = 'black').grid(row = 1,column = 2, sticky = W)
    Label(P_INFO, text = Lista[0][i][4], font = ('Arial',9),fg = 'black').grid(row = 1,column = 3, sticky = W)
    Label(P_INFO, text = Lista[0][i][5], font = ('Arial',9),fg = 'black').grid(row = 1,column = 4, sticky = W)
    Label(P_INFO, text = Lista[0][i][6], font = ('Arial',9),fg = 'black').grid(row = 1,column = 5, sticky = W)

    Label(P_INFO, text = "Cambio de datos:", font = ('Arial',10),fg = 'black').grid(row = 2,column = 0, sticky = W)
    
    e1 = Entry(P_INFO)
    e2 = Entry(P_INFO)
    e3 = Entry(P_INFO)
    e4 = Entry(P_INFO)
    e5 = Entry(P_INFO)
    e6 = Entry(P_INFO)
    
    e1.grid(row = 3,column = 0)
    e2.grid(row = 3,column = 1)
    e3.grid(row = 3,column = 2)
    e4.grid(row = 3,column = 3)
    e5.grid(row = 3,column = 4)
    e6.grid(row = 3,column = 5)

    B_GUARDAR = Button(P_INFO,text = 'Guardar Cambios',command=lambda:Cambios(Lista),fg='white', bg = 'black', font = ('Arial',12))
    B_GUARDAR.place(x = 5, y = 250)

    B_Cancelar = Button(P_INFO,text = 'Cancelar',command=lambda:Buscar_inicio(),fg='white', bg = 'black', font = ('Arial',12))
    B_Cancelar.place(x = 5,y = 285)

ventana_inicio()
