#!/usr/bin/python3

import numpy as np							#Importação dos comandos dentro da biblioteca numpy
import matplotlib.pyplot as plt						#Importação dos comandos dentro da biblioteca matplotlib.pyplot
from settings import *							#Importaçao de todos os dados da biblioteca settings (configurações)

def f(t, x, u):								#Definição de uma função de entrada dos vetores de t, x e u
    # Vetor de Estado
    x1 = x[0]								#Atribuição a variável x1 da primeira coluna de x
    x2 = x[1]								#Atribuição a variável x2 da segunda coluna de x

    x_dot = np.array( [x2, \
    (-p*l1/J)*np.sin(x1) + (-ua/J)*x2 + (l2/J)*u], dtype='float64')	#Atribuição na variável x_dot da discretização da equação do pendulo

    return x_dot							#Retorno do valor da variável x_dot

#Runge Kutta de 4ª órdem
def rk4(tk, h, xk, uk):							#Definição de uma função de entrada dos valores dos vetores t, h, x e u
    k1 = f(tk		, xk		, uk)				#Chama da função f para obtenção do valor da inclinação do início do intervalo
    k2 = f(tk + h/2.0	, xk + h*k1/2.0	, uk)				#Chama da função f para obtenção do valor da inclinação do ponto médio do intervalo
    k3 = f(tk + h/2.0	, xk + h*k2/2.0	, uk)				#Chama da função f para obtenção do valor da inclinação do ponto médio do intervalo
    k4 = f(tk + h	, xk + h*k3	, uk)				#Chama da função f para obtenção do valor da inclinação do final do intervalo

    xkp1 = xk + (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)				#Atribuição na variável xkp1 do valor da aproximação

    return xkp1								#Retorna o valor da variável xkp1

def simulacao(theta):							#Definição de uma função de chamada para execução do código
    ek_1 = 0								#

    # PARÂMETROS DE SIMULAÇÃO
    t = np.arange(0,5,h)						#Declaração do vetor tempo
    tam = len(t)							#Números de variáveis do vetor tempo criado

    # Vetor de estados
    x = np.zeros([2, tam],dtype='float64')				#Criação de uma matrix com 2 colunas e números de linhas iguais ao número de variáveis do vetor tempo

    # Determinar um valor para a força de controle de equilíbrio
    u_ref = np.sin(theta*np.pi/180)*p*l1/l2				#Criação de uma equação de onde o sistema entra em equilíbrio
    #u = u_ref*np.ones([tam],dtype='float64')

    # Entrada do Sistema compensado
    the_ref = theta*np.pi/180.0						#Criação do ângulo de equilíbrio
    u = np.zeros([tam],dtype='float64')					#Criação do vetor u de controle do ângulo
    e = np.zeros([tam],dtype='float64')

    #Ganhos tustin
    kp = 10
    ki = 1
    kd = 1.5e+3

    # Execução da simulação
    for k in range(tam-1):						#Loop de integração do valor de x
	#Aplicação do PID pelo metodo de discretização de tustin
        e[k] = the_ref - x[0][k]
        u[k] = kp*e[k] + ki*(e[k] + ek_1) + kd*(e[k] - ek_1) + u_ref
        ek_1 = e[k]

        # Atualização do estado
        x[:,k+1] = rk4(t[k], h, x[:,k], u[k])				#Chamada da função de rugen kutta para retorno do valor de x

    return t,x								#Retorno do vetor t e x

if __name__ == '__main__':						#Verificação se a biblioteca atual é a principal
  t,x = simulacao(30)							#Atribuição das variáveis t e x retornadas na chamada da função simulacao

  plt.subplot(2,1,1)							#Definição de duas áreas de plotagem, um sobre o outro, onde iremos atribui o primeiro plot
  plt.plot(t,x[0,:]*180/np.pi)						#Definição da plotagem da variável ângulo em graus por tempo
  plt.ylabel('$x_1$ - i')						#Definição do texto do eixo y
  plt.subplot(2,1,2)							#Definição de duas áreas de plotagem, um sobre o outro, onde iremos atribui o segundo plot
  plt.plot(t,x[1,:]*180/np.pi)						#Definição da plotagem da variável velocidade ângular por tempo
  plt.ylabel('$x_2$ - q')						#Definição do texto do eixo y
  plt.xlabel('t [s]')							#Definição do texto do eixo x
  plt.show()								#Comando para apresentar a imagem do plot
