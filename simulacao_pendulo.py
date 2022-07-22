#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def f(t, x, u):
# State vector
# x = [x2 x1]^T
    x1 = x[0]
    x2 = x[1]
    l1 =.75
    l2 = 1.2
    J = 1e-2
    p = .85*9.81
    ua = .1
    x_dot = np.array( [0 + x2, (-p*l1/J)*np.sin(x1) + (-ua/J)*x2 + (l2/J)*u ], dtype='float64')
    return x_dot

# Runge Kutta de 4ª órdem
def rk4(tk, h, xk, uk):
    #xk = xk.reshape([2,1])
    #uk = uk.reshape([1,1])
    k1 = f(tk , xk , uk)
    k2 = f(tk + h/2.0, xk + h*k1/2.0, uk)
    k3 = f(tk + h/2.0, xk + h*k2/2.0, uk)
    k4 = f(tk + h , xk + h*k3 , uk)
    xkp1 = xk + (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)
    return xkp1 #.reshape([2,])



def simulacao():
    
    # PARÂMETROS DE SIMULAÇÃO
    h = 1e-4 # Sample time
    t = np.arange(0,5,h) # vetor tempo
    tam = len(t)
    # Vetor de estados
    x = np.zeros([2, tam],dtype='float64')
    #x[:,0] = np.array([20*np.pi/180.,0]) # Condição Inicial

    # Determinar um valor para a força de controle de equilíbrio
    l1 =.75
    l2 = 1.2
    J = 1e-2
    p = .85*9.81
    u_eq = np.sin(30*np.pi/180)*p*l1/l2
    # Vetor de entrada
    u = u_eq*np.ones([tam],dtype='float64')

    # Execução da simulação
    for k in range(tam-1):
        # u(k) será calculado aqui na simulação
        
        # Atualização do estado
        x[:,k+1] = rk4(t[k], h, x[:,k], u[k])
    
    return t,x
        
    
if __name__ == '__main__':

    t,x = simulacao()
    plt.subplot(2, 1, 1)
    plt.plot(t,x[0,:]*180/np.pi)
    plt.ylabel('$x_1$ - i ')
    plt.subplot(2, 1, 2)
    plt.plot(t,x[1,:]*180/np.pi)
    plt.ylabel('$x_2$ - q')
    plt.xlabel('t [s]')
    plt.show()


''' y[n] =  10.77*x[n]-19,43*x[n-1]+9,102*x[n-2]+1.593*y[n-1]+0.5931*y[n-2]1'''
