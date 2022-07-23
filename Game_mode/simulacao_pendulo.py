#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from settings import *

def f(t, x, u):
    # Vetor de Estado
    x1 = x[0]								#
    x2 = x[1]								#

    x_dot = np.array( [x2, \
    (-p*l1/J)*np.sin(x1) + (-ua/J)*x2 + (l2/J)*u], dtype='float64')	#

    return x_dot							#

#Runge Kutta de 4ª órdem
def rk4(tk, h, xk, uk):							#
    k1 = f(tk		, xk		, uk)				#Chama da função f para obtenção do valor de
    k2 = f(tk + h/2.0	, xk + h*k1/2.0	, uk)				#
    k3 = f(tk + h/2.0	, xk + h*k2/2.0	, uk)				#
    k4 = f(tk + h	, xk + h*k3	, uk)				#

    xkp1 = xk + (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)				#

    return xkp1								#

def simulacao():							#
    # PARÂMETROS DE SIMULAÇÃO
    t = np.arange(0,5,h)						#Declaração do vetor tempo
    tam = len(t)							#Números de variáveis do vetor tempo criado

    # Vetor de estados
    x = np.zeros([2, tam],dtype='float64')				#Criação de uma matrix com duas colunas e números de linhas iguais ao número de variáveis do vetor tempo

    # Determinar um valor para a força de controle de equilíbrio
    u_eq = np.sin(theta*np.pi/180)*p*l1/l2				#

    # Vetor de entrada
    u = u_eq*np.ones([tam],dtype='float64')				#

    # Execução da simulação
    for k in range(tam-1):						#
        # Atualização do estado
        x[:,k+1] = rk4(t[k], h, x[:,k], u[k])				#

    plt.subplot(2,1,1)
    plt.plot(t,x[0,:]*180/np.pi)
    plt.ylabel('$x_1$ - i')
    plt.subplot(2,1,2)
    plt.plot(t,x[1,:]*180/np.pi)
    plt.ylabel('$x_2$ - q')
    plt.xlabel('t [s]')
    plt.show()

    print(tam)

    return tam,x
