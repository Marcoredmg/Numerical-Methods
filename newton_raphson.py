#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *
import math
from Tkinter import *
import tkSimpleDialog

def NewtonRaphson():
	funcion = str(tbFuncion.get())
	valor_inicial = str(tbXi.get())
	error_deseado = float(tbError.get())
	max_iteraciones = int(tbIter.get())

	funcion = funcion.replace("X","y")

	aux = 0.0
	xi = float(valor_inicial)
	fd = diff(funcion)
	fd = str(fd)

	for i in range(max_iteraciones):
		
		fxi = funcion.replace("log", "math.log")
		fxi = funcion.replace("exp", "math.exp")
		fxi = eval(fxi.replace("y", str(xi)))

		dfxi = fd.replace("exp", "math.exp")
		dfxi = eval(dfxi.replace("y", str(xi)))

		xi1 = xi - (float(fxi)/float(dfxi))

		print "%f - ( %f / %f )" % (xi,fxi,dfxi)
		print "xi+1 = %f en iteracion %i" % (xi1, i)
		
		error = ((xi1 - xi) / xi1) * 100
		error = abs(error)
		print "error = %f" % error
		
		xi = float(xi1)
		if(error < error_deseado):
			break

	aux_resultado = "La aproximacion a la raiz es: " + str(xi)
	aux_error = "La aproximacion del errore es: " + str(error)

	print "La aproximacion a la raiz es: %f" % xi
	print "Con un error estimado de: %f" % error
	
	aprox_resultado.config(text=aux_resultado)
	aprox_error.config(text=aux_error)


app = Tk()
app.title("Metodo de Newton-Raphson")

index = Frame(app)
index.grid(row=0, column=0, padx=(150, 150), pady=(100, 100))
index.columnconfigure(0, weight=1)
index.rowconfigure(0, weight=1)

titulo = Label(index,text="Metodo de Newton-Raphson")
titulo.grid(row=1, column=1)

etiqueta1 = Label(index, text="Ingrese funcion en x a evaluar(INGRESE LA X EN MAYUSCULA): ")
etiqueta1.grid(row=2, column=1)

funcion = ""
tbFuncion = Entry(index, width=10, textvariable=funcion)
tbFuncion.grid(row=3, column=1)

etiqueta2 = Label(index, text="Ingrese valor para xi: ")
etiqueta2.grid(row=4, column=1)

xi = 0.0
tbXi = Entry(index, width=10, textvariable=xi)
tbXi.grid(row=5, column=1)

etiqueta3 = Label(index, text="Ingrese error deseado: ")
etiqueta3.grid(row=6, column=1)

error = 0.01
tbError = Entry(index, width=8, textvariable=error)
tbError.grid(row=7, column=1)

etiqueta3 = Label(index, text="Ingrese maximo de iteraciones: ")
etiqueta3.grid(row=8, column=1)

max_iteraciones = 0
tbIter = Entry(index,width=8, textvariable=max_iteraciones)
tbIter.grid(row=9, column=1)

boton = Button(index, text="OK", command=NewtonRaphson)
boton.grid(row=10, column=1)

aprox_resultado = Label(index, text="")
aprox_resultado.grid(row=11, column=1)

aprox_error = Label(index, text="")
aprox_error.grid(row=12, column=1)

app.mainloop()