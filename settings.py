#!/usr/bin/python3

#Configurações Iniciais
WIDTH	= 800			#Comprimento da Tela
HEIGHT	= 640			#Altura da Tela
FPS	= 60			#Numero de Telas por Segundo
#TILESIZE = 64 #Tamnho do Ladrilho (Malha)

#Dados de Entrada
h 	= 1e-4			#Declaração da variável de divisão do tempo

l1	= 0.75			#Declaração da posição do centro de massa do pendulo
l2	= 1.2 * 30		#Declaração do comprimento do pendulo

J	= 1e-2			#Declaração do momento angular do pendulo

mp	= 0.85			#Declaração da massa do conjunto
g	= 9.81			#Aceleração da gravidade padrão
p	= mp * g		#Calculo da força peso aplicada sobre o pendulo

ua	= 0.1			#Declaração do coeficiente de atrito

