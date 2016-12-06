import sys
from Tkinter import *
import tkSimpleDialog

def InterpolacionNewton():
	n = int(opcion.get())
	niveles = [0.0] * n
	for i in range(n):
	    niveles[i] = [0.0] * n

	vector_x = [0.0] * n

	print niveles
	print vector_x
	for i in range(n):
	    x = tkSimpleDialog.askfloat("","Ingrese el valor de x: ")
	    aux = str(x)
	    y = tkSimpleDialog.askfloat("","Ingrese el valor de f("+aux+"): ")
	    vector_x[i] = float(x)
	    niveles[i][0] = float(y)

	print vector_x   
	print niveles

	punto_a_evaluar = float(tkSimpleDialog.askfloat("","Ingrese el punto a evaluar: "))

	
	print "-----------------------------1------------------------------"
	print "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"

	for i in range(1,n):
	    for j in range(i,n):

	        print "*****************************************"
	        
	        niveles[j][i] = ( (niveles[j][i-1]-niveles[j-1][i-1]) / (vector_x[j]-vector_x[j-i]))

	print "-----------------------------2------------------------------"
	print "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
	for i in range(n):
		print niveles[i]	
	aprx = 0
	aux_mul = 1.0
	for i in range(n):
	    aux_mul = niveles[i][i];
	    for j in range(1,i+1):
	        aux_mul = aux_mul * (punto_a_evaluar - vector_x[j-1])
	    aprx = aprx + aux_mul

	
	aux1 = str(punto_a_evaluar)
	aux2 = str(aprx)
	resultado = "Valor aproximado de f("+aux1+") es: "+ aux2
	valor_apprx.config(text=resultado)


app = Tk()
app.title("Interpolacion de Newton")

index = Frame(app)
index.grid(row=0, column=0, padx=(80, 80), pady=(50, 50))
index.columnconfigure(0, weight=1)
index.rowconfigure(0, weight=1)

titulo = Label(index,text="Interpolacion de Newton")
titulo.grid(row=1, column=1)

etiqueta1 = Label(index,text="Introduce el numero de etapas con el que vas a trabajar:")
etiqueta1.grid(row=2, column=1)

n = 0
opcion = Entry(index, width=10, textvariable=n)
opcion.grid(row=3, column=1)

valor_apprx = Label(index,text="")
valor_apprx.grid(row=4, column=1)

matriz = Label(index, text="")
matriz.grid(row=5, column=1)

boton = Button(index, text="OK", command=InterpolacionNewton)
boton.grid(row=6, column=1)

app.mainloop()