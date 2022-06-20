# Control Canvas

# Permitir acceder a una serie de primitivas gr�ficas: lineal, rect�ngulos, ovalos, etc.

import tkinter as tk
from tkinter import ttk as ttk


class Aplicacion:
    def __init__(self):
        self.formulario=tk.Tk()
        self.entradadatos()
        self.canvas1=tk.Canvas(self.formulario, width=800, height=600, background="black")
        self.canvas1.grid(column=0,row=1)

        self.formulario.mainloop()

    def entradadatos(self):
        self.lf1=ttk.LabelFrame(self.formulario, text="Equipos de Futbol")
        self.lf1.grid(column=0,row=0,sticky="w")

        self.label1=ttk.Label(self.lf1, text="Sporting Cristal")
        self.label1.grid(column=0,row=0,padx=5,pady=5)

        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.lf1, textvariable=self.dato1)
        self.entry1.grid(column=1,row=0,padx=5,pady=5)

        self.label2=ttk.Label(self.lf1, text="Alianza Lima")
        self.label2.grid(column=0,row=1,padx=5,pady=5)

        self.dato2=tk.StringVar()
        self.entry2=ttk.Entry(self.lf1, textvariable=self.dato2)
        self.entry2.grid(column=1,row=1,padx=5,pady=5)

        self.label3=ttk.Label(self.lf1, text="Universitario")
        self.label3.grid(column=0,row=2,padx=5,pady=5)

        self.dato3=tk.StringVar()
        self.entry3=ttk.Entry(self.lf1, textvariable=self.dato3)
        self.entry3.grid(column=1,row=2,padx=5,pady=5)

        self.btnGenerarGrafico=ttk.Button(self.lf1,text="Generar Gr�fico",command=self.grafico)
        self.btnGenerarGrafico.grid(column=0,row=3, columnspan=2, padx=5, pady=5, sticky="we")

        self.entry1.focus()
    
    def grafico(self):
        self.canvas1.delete(tk.ALL)
        valor1=int(self.dato1.get())
        valor2=int(self.dato2.get())
        valor3=int(self.dato3.get())

        #calculando las barras
        ValorT=float(valor1+valor2+valor3)
        largo1=(valor1*100/ValorT)*7
        largo2=(valor2*100/ValorT)*7
        largo3=(valor3*100/ValorT)*7

        
        pr1=str(round(valor1*100/ValorT,2))
        pr2=str(round(valor2*100/ValorT,2))
        pr3=str(round(valor3*100/ValorT,2))
        

        #Dibujar las barras
        self.canvas1.create_rectangle(10,10,10+largo1,90,fill="red")
        self.canvas1.create_rectangle(10+largo1,10,10+largo1+largo2,90,fill="green")
        self.canvas1.create_rectangle(10+largo1+largo2,10,10+largo1+largo2+largo3,90,fill="blue")
        #Mostrar el texto a lado de la barra
        self.canvas1.create_text(largo1-35,100,text=pr1+"% SC", fill="white",font="Arial")
        self.canvas1.create_text(largo1+largo2-35,100,text=pr2+"% AL", fill="white",font="Arial")
        self.canvas1.create_text(largo1+largo2+largo3-35,100,text=pr3+"% U", fill="white",font="Arial")

aplicacion1=Aplicacion()
