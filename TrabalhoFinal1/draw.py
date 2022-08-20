#!/usr/bin/python3

import pygame, math								#Importação dos comandos dentro das bibliotecas pygame e math (matemática)
import simulacao_pendulo as simup						#Importação dos comandos dentro da biblioteca simulacao_pendulo como simup
from settings import *								#Importação de todos os dados da biblioteca settings (configurações)
from button import Button							#
from teste import Teste

class Draw:									#Definição de classe para chamadas
  def __init__(self):								#Definição de uma função da chamada inicial
    #Pega as informações da superficie
    self.display_surface = pygame.display.get_surface()				#Capturando a superfície da tela pygame aberta

    #Definições para desenho
    self.center = (WIDTH/2,HEIGHT/3)						#Definição do ponto onde o pendulo é fixo

    self.teste = Teste()

  def run(self, i, count1, count2, w):						#Definição da função de execução da biblioteca level
    for j in range(25,WIDTH,25):						#Loop para desenho das grids verticais do desenho
      pygame.draw.lines(self.display_surface,'gray',False,[(j,0),(j,HEIGHT)])	#Chamada para desenho de linhas verticais
    for k in range(25,HEIGHT,25):						#Loop para desenho da grids horizontais do desenho
      pygame.draw.lines(self.display_surface,'gray',False,[(0,k),(WIDTH,k)])	#Chamada para desenho de linhas horizontais

    if count1 == 0:
      theta_text, count2, w = self.teste.entrada(count2, w)
      theta = float(theta_text)
      self.mat, self.x = simup.simulacao(theta)					#Chamada das variáveis de tamanho da matrix e do valor do vetor x na biblioteca simup
      count1 = 1
    else:
      self.teste.entrada(count2, w)

    pos = (round(self.center[0] + l2*300*math.sin(self.x[0,i])), \
    round(self.center[1] + l2*300*math.cos(self.x[0,i])))			#Definição da posição da extremidade movél do pendulo

    aux = str(round(self.x[0,i]*180/math.pi)) + '°'				#Variável auxiliar para obtenção do ângulo em graus
    self.theta = Button(pygame.transform.scale(pygame.image.load("Image/quad1.png"), \
    (300,80)),(WIDTH/2,HEIGHT/5),aux,get_font(75),"black","black")		#Variável para desenho de uma caixa com os valores de ângulo do pendulo

    if i < len(self.mat) - 1:							#Verificação da posição i dentro do vetor x para debug
      i += 1									#Incremento de uma unidade na variável i

    pygame.draw.circle(self.display_surface,'black',self.center,4)		#Chamada para desenho do ponto onde o pendulo é fixo
    pygame.draw.line(self.display_surface,'black',self.center,pos,2)		#Chamada para desenho da haste do pendulo
    pygame.draw.circle(self.display_surface,'black',pos,20)			#Chamada para desenho do contorno do ponto móvel do pendulo
    pygame.draw.circle(self.display_surface,'red',pos,18)			#chamada para prenchimento do interior do ponto móvel do pendulo

    self.theta.update(self.display_surface)					#Chamada da função update na classe Button

    return i, count1, count2, w							#Retorno do valor da variável i incrementada

#Definição da Fonte
def get_font(size):								#Definição de uma função para chamada de mudança de fonte
  return pygame.font.Font("Font/font.ttf", size)				#Retorna o valor as predefinições do tamanho e o tipo de fonte
