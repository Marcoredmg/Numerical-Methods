#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from Tkinter import *
import tkSimpleDialog
def Simpson():
	n = int(npuntos.get())

	puntos = []


	numero_trapecios = n - 1

	for i in range(n):
		y = tkSimpleDialog.askfloat("","Ingrese el valor de f(x): ")
		puntos.append(y)

	print puntos

	suma = 0.0

	a = tkSimpleDialog.askfloat("","Ingrese limite inferior: ")
	b = tkSimpleDialog.askfloat("","Ingrese limite superior: ")


	if(a == b):
		print "Los limites no pueden ser iguales"
	elif(a > b):
		auxiliar = a
		a = b
		b = auxiliar
		

	print a
	print b

	if(numero_trapecios % 2 == 0):
		
		h = (b - a) / numero_trapecios
		j = 0
		for i in range(1,numero_trapecios,2):
			suma = suma + (h/3) * (puntos[j] + (4 * puntos[i]) + (puntos[i + 1]))
			j = j + 2


	elif(numero_trapecios % 3 == 0):
		
		h = (b - a) / numero_trapecios
		j = 0
		for i in range(1,numero_trapecios - 1,3):
			suma = suma + ((3 * h) / 8) * (puntos[j] + (3 * puntos[i]) + (3 * puntos[i + 1]) + puntos[i + 2])
			j = j + 3

	else:
		h = (b - a) / numero_trapecios

		aux = a + (3 * h) 

		h13 = (b - aux) / (n - 4)
		h38 = (aux - a) / 3

		
		suma = ((3 * h38) / 8) * (puntos[0] + (3 * puntos[1]) + (3 * puntos[2]) + puntos[3])
		print suma
		j = 3
		k = 4
		for i in range(4, numero_trapecios, 2):
			impresion = (h13/3) * (puntos[j] + 4 * (puntos[k]) + (puntos[k + 1]))
			print (impresion)
			suma = suma + (h13/3) * (puntos[j] + 4 * (puntos[k]) + (puntos[k + 1]))
			j = j + 2
			k = k + 1
	aux_impresion = str(suma)
	resultado_final = "Valor arpoximado: " + aux_impresion
	valor.config(text=resultado_final)

app = Tk()
app.title("Integracion numerica Simpson")

index = Frame(app)
index.grid(row=0, column=0, padx=(80,80), pady=(50,50))
index.columnconfigure(0,weight=1)
index.rowconfigure(0,weight=1)

titulo = Label(index, text="Integración numerica Simpson")
titulo.grid(row=1,column=1)

etiqueta1 = Label(index,text="Introduce el numero de puntos")
etiqueta1.grid(row=2,column=1)

n = 0
npuntos = Entry(index, width=10, textvariable=n)
npuntos.grid(row=3, column=1)

valor = Label(index, text="")
valor.grid(row=4, column=2)

boton = Button(index, text="OK", command=Simpson)
boton.grid(row=6, column=1)

app.mainloop()
