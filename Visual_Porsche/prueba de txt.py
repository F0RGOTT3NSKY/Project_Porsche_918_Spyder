





'''
archivo=open('datos.txt','w')

nombre=input('Nombre:')
archivo.write(nombre+'\t')
numero=int(input('introduce el numero:'))
archivo.write(str(numero)+'\t')
n=int(input('Cuantos deportes?'))
deportes=[]
for i in range(n):
        deporte=input('Deporte: ')
        deportes.append(deporte)
archivo.write('deportes=%s'%deportes)
        op
archivo.close()
'''

def leer():
   
    file=open('porsche_datos.txt','r')
    texto=file.read()
    datos=eval(texto)
    file.close()
    return datos[0]
