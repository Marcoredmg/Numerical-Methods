#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *
import math

def NewtonRaphson():
	funcion = raw_input("ingrese una funcion donde x es la variable a evaluar: ")
	valor_inicial = raw_input("ingrese valor inicial: ")
	error_deseado = float(raw_input("ingrese error deseado: "))
	max_iteraciones = int(raw_input("ingrese maximo de iteraciones: "))

	funcion = funcion.replace("x","y")

	aux = 0.0
	xi = float(valor_inicial)
	fd = diff(funcion)
	fd = str(fd)
	for i in range(max_iteraciones):
		
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
	print "La aproximacion a la raiz es: %f" % xi
	print "Con un error estimado de: %f" % error



NewtonRaphson()