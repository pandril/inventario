from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter import *
import csv

def agregar():
    if campo3.get()=='comida':
        sumar("comida.txt")

    elif campo3.get()=='herramienta':
        sumar("herramienta.txt")

    elif campo3.get()=='bienes':
        sumar("bienes.txt")

    else:
        messagebox.showinfo('Error','Debe ingresar el tipo de Rublo')
                
def restar():
    if campo3.get()=='comida':
        sustracion("comida.txt")

    elif campo3.get()=='herramienta':
        sustracion("herramienta.txt")

    elif campo3.get()=='bienes':
        sustracion("bienes.txt")

    else:
        messagebox.showinfo('Error','Debe ingresar el tipo de Rublo')

def sumar(listaTexto):
    print ("inicio")
    with open(listaTexto,"r+") as f:
        lectura=f.readlines()
        print(lectura)
        lecturaRublo=[]     
        for x in lectura:
            RubloSolo=x.split(", ")
            lecturaRublo.append(RubloSolo[0])
        print (lecturaRublo)     
        tamanoRublo=len(campo1.get())

        
        
        lectura2Rublo=[]
        for x in lectura:
            RubloSolo=x.split(", ")
            lectura2Rublo.append(RubloSolo)
       
        if campo1.get() in lecturaRublo:
            for indice,valor in enumerate(lectura):
                
                if valor[:tamanoRublo] == campo1.get():
                    
                    suma=str(int(lectura2Rublo[indice][1])+int(campo2.get()))
                    lectura[indice]=campo1.get()+", "+suma+", "+campo4.get()+", "+ campo5.get()+"\n"
                    
                else:
                    pass
        else:
            nuevoRublo=campo1.get()+", "+campo2.get()+", "+campo4.get()+", "+ campo5.get()+"\n"
            lectura.append(nuevoRublo)
        print (lectura)
        lectura= sorted(lectura)
        lectura2=""
        for x in lectura:
            lectura2=lectura2+x
            with open(listaTexto,"w") as a:
                a.write(lectura2)
            a.close()
    f.close()

def sustracion(listaTexto):
    print ("inicio sustracion")
    with open(listaTexto,"r+") as f:
        lectura=f.readlines()
        print(lectura)
        lecturaRublo=[]
       
        for x in lectura:
            RubloSolo=x.split(", ")
            lecturaRublo.append(RubloSolo[0])
     
        tamanoRublo=len(campo1.get())
        cantidadExacta= tamanoRublo+2

        lectura2Rublo=[]
        for x in lectura:
            RubloSolo=x.split(", ")
            lectura2Rublo.append(RubloSolo)
       
        if campo1.get() in lecturaRublo:
            for indice,valor in enumerate(lectura):
                
                if valor[:tamanoRublo] == campo1.get():
                    
                    suma=str(int(lectura2Rublo[indice][1])-int(campo2.get()))
                    lectura[indice]=campo1.get()+", "+suma+", "+campo4.get()+", "+ campo5.get()+"\n"
                    
                else:
                    pass
        else:
            messagebox.showinfo('Error','Elemento no existente en Inventario')
        print (lectura)
        lectura= sorted(lectura)
        lectura2=""
        for x in lectura:
            lectura2=lectura2+x
            with open(listaTexto,"w") as a:
                a.write(lectura2)
            a.close()
    f.close()


def mostrar():
    if campo3.get()=='comida':
        mostrar2("comida.txt")

    elif campo3.get()=='herramienta':
        mostrar2("herramienta.txt")

    elif campo3.get()=='bienes':
        mostrar2("bienes.txt")

    else:
        messagebox.showinfo('Error','Debe ingresar el tipo de Rublo')

def mostrar2(listaTexto):
    with open(listaTexto,"r") as f:

        ventana2=tk.Tk()

        etiqueta4= tk.Label(ventana2, text=f.read())
        etiqueta4.grid(row=1,column=1)

        ventana2.mainloop()
    f.closed



impresion=open("comida.txt","r+")
impresion2=open("herramienta.txt","r+")
impresion3=open("bienes.txt","r+")
impresionRublos=impresion.readlines()
impresionRublos2=impresion2.readlines()
impresionRublos3=impresion3.readlines()
impresionRublofinal=[]

for x in impresionRublos:
    RubloSolo = x.split(', ')
    impresionRublofinal.append(RubloSolo[0])
for x in impresionRublos2:
    RubloSolo = x.split(', ')
    impresionRublofinal.append(RubloSolo[0])
for x in impresionRublos3:
    RubloSolo = x.split(', ')
    impresionRublofinal.append(RubloSolo[0])
rublosOrdenados=sorted(impresionRublofinal)
print(rublosOrdenados)



ventana=tk.Tk()
ventana.title('Inventario')

etiqueta1=tk.Label(ventana, text='Ingrese Rublo:')
etiqueta1.grid(row=3,column=1)

campo1=ttk.Combobox(ventana,textvariable='comida', values=impresionRublofinal, state="normal")
campo1.grid(row=3,column=2)

etiqueta2=tk.Label(ventana, text='Ingrese Cantidad:')
etiqueta2.grid(row=4,column=1)

campo2=tk.Entry(ventana)
campo2.grid(row=4,column=2)

etiqueta3=tk.Label(ventana, text='Tipo de Rublo:')
etiqueta3.grid(row=2,column=1)

campo3=ttk.Combobox(ventana,textvariable='Tipo de Rublo', values=['comida','herramienta','bienes'], state="readonly")
campo3.grid(row=2,column=2)

etiqueta4=tk.Label(ventana, text='Ubicacion:')
etiqueta4.grid(row=5,column=1)

campo4=tk.Entry(ventana)
campo4.grid(row=5,column=2)

etiqueta5=tk.Label(ventana, text='Caracteristica:')
etiqueta5.grid(row=6,column=1)

campo5=tk.Entry(ventana)
campo5.grid(row=6,column=2)

boton1=tk.Button(ventana, text='Agregar', command= agregar)
boton1.grid(row=7,column=1)

boton3=tk.Button(ventana, text='Restar', command= restar)
boton3.grid(row=7,column=2)

boton2=tk.Button(ventana, text='Inventario', command= mostrar)
boton2.grid(row=8,column=2)


ventana.mainloop()


