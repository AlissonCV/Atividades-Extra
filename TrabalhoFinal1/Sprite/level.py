#!/usr/bin/python3

import pygame, math								#Importação dos comandos dentro das bibliotecas pygame e math (matemática)
import simulacao_pendulo as simup						#Importação dos comandos dentro da biblioteca simulacao_pendulo como simup
from settings import *								#Importação de todos os dados da biblioteca settings (configurações)
from image import Image

class Level:									#Definição de classe para chamadas
  def __init__(self):								#Definição de uma função da chamada inicial
    #Pega as informações da superficie
    self.display_surface = pygame.display.get_surface()				#Capturando a superfície da tela pygame aberta

    #Definições para desenho
    self.center = (WIDTH/2,100)							#Definição do ponto onde o pendulo é fixo
    self.len, self.x = simup.simulacao()					#Chamada das variáveis de tamanho da matrix e do valor do vetor x na biblioteca simup
    self.i = 0									#Definição da variável i como a primeira posição do vetor x
    self.aux = 0								#Definição da variável auxiliar para debug

    #Grupo de configurações de sprite
    self.sprite = pygame.sprite.Group()

  def run(self):								#Definição da função de execução da biblioteca level
    for j in range(25,WIDTH,25):						#Loop para desenho das grids verticais do desenho
      pygame.draw.lines(self.display_surface,'gray',False,[(j,0),(j,HEIGHT)])	#Chamada para desenho de linhas verticais
    for k in range(25,HEIGHT,25):						#Loop para desenho da grids horizontais do desenho
      pygame.draw.lines(self.display_surface,'gray',False,[(0,k),(WIDTH,k)])	#Chamada para desenho de linhas horizontais

    pos = (round(self.center[0] + l2*math.sin(self.x[0,self.i])), \
    round(self.center[1] + l2*math.cos(self.x[0,self.i])))			#Definição da posição da extremidade movél do pendulo
    if self.i < self.len - 1:							#Verificação da posição i dentro do vetor x para debug
      self.i += 1								#Incremento de uma unidade na variável i
    elif self.aux == 0:								#Verificação auxiliar de termino do loop
      print('Fim')								#Printagem no terminal do fim da variação na posição do pendulo
      self.aux = 1								#Comfirmação pela variável auxiliar que o loop terminou

    self.image = Image(self.center, pos, self.sprite)

    self.sprite.custom_draw(self.image)
    self.sprite.move()
#    pygame.draw.circle(self.display_surface,'black',self.center,4)		#Chamada para desenho do ponto onde o pendulo é fixo
#    pygame.draw.line(self.display_surface,'black',self.center,pos,2)		#Chamada para desenho da haste do pendulo
#    pygame.draw.circle(self.display_surface,'black',pos,20)			#Chamada para desenho do contorno do ponto móvel do pendulo
#    pygame.draw.circle(self.display_surface,'red',pos,18)			#chamada para prenchimento do interior do ponto móvel do pendulo
