#! /usr/bin/env python
# -*- coding: utf-8 -*-
import math
from sympy import *
from Tkinter import *
import tkSimpleDialog

def Secante():
	fx = str(tbFuncion.get())
	xi = tkSimpleDialog.askfloat("","Ingrese el valor de xi: ")
	ximenosuno = tkSimpleDialog.askfloat("","Ingrese el valor de xi - 1: ")
	ep = float(tbError.get())
	maxiter = int(opcion.get())

	fx = fx.replace("log", "math.log")
	fx = fx.replace("exp", "math.exp")
	fx = fx.replace("X","y")

	for i in range(maxiter):
			
		fxi = eval(fx.replace("y", str(xi)))
		fximenosuno = eval(fx.replace("y", str(ximenosuno)))
		
		resultado = xi - ((fxi * (ximenosuno - xi)) / (fximenosuno - fxi))
		
		errorP = ((resultado - xi)/resultado)*100
		errorP = abs(errorP)

		xi = resultado
		ximenosuno = fximenosuno

		if(errorP < ep):
			break

	aux = "El resultado arpoximado es de: " + str(resultado)
	aux_error = "El error aproximado es de: " + str(errorP) + "%"

	print "El resultado es: %f" % resultado
	print "Con un error de: %f" % errorP
	
	aprox_resultado.config(text=aux)
	aprox_error.config(text=aux_error)

app = Tk()
app.title("Metodo de la secante")

index = Frame(app)
index.grid(row=0, column=0, padx=(150, 150), pady=(100, 100))
index.columnconfigure(0, weight=1)
index.rowconfigure(0, weight=1)

titulo = Label(index, text="Metodo de la secante")
titulo.grid(row=1,column=1)

etiqueta1 = Label(index,text="Introduce la funcion en X a evaluar (INGRESE LA X EN MAYUSCULA):")
etiqueta1.grid(row=2, column=1)

fx = ""
tbFuncion = Entry(index, width=15, textvariable=fx)
tbFuncion.grid(row=3, column=1)

etiqueta2 = Label(index, text="Introduce el numero de etapas: ")
etiqueta2.grid(row=4, column=1)

maxiter = 0
opcion = Entry(index, width=10, textvariable=maxiter)
opcion.grid(row=5, column=1)


etiqueta3 = Label(index, text="Introduce el error deseado: ")
etiqueta3.grid(row=7, column=1)

ep = 0.001
tbError = Entry(index, width=11, textvariable=ep)
tbError.grid(row=8, column=1)

boton = Button(index, text="OK", command=Secante)
boton.grid(row=9, column=1)

aprox_resultado = Label(index, text="")
aprox_resultado.grid(row=11, column=1)

aprox_error = Label(index, text="")
aprox_error.grid(row=12, column=1)

app.mainloop()
				









