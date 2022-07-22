#!/usr/bin/python3

import pygame, sys
from settings import *
from grid import Grid
#from draw import Draw

class Pendulo:
  def __init__(self):
    #Configurações Gerais
    pygame.init()                                               #Inicialização da biblioteca pygame
    self.screen = pygame.display.set_mode((WIDTH,HEIGHT)) #Criação de uma superfície de exibi>
    pygame.display.set_caption('Inverted Pendulum Control')     #Alteração do título da janela
    self.clock = pygame.time.Clock()                            #Criação de um relógio
    #são configurações básicas necessarias para rodar a biblioteca pygame

    self.grid = Grid()
#    self.draw = Draw()

  def run(self):						#Definição de uma função de execução
    while True:							#Criação de um loop infinito de ver>
      for event in pygame.event.get():				#Criação de uma verificação de even>
        if event.type == pygame.QUIT:				#Verificando se o evento solicitado>
          pygame.quit()						#Fechamento do jogo
          sys.exit()						#Fechamento da execução

      self.screen.fill('white')                           #Preenchimento da tela com a cor preta
      self.grid.run()
#      self.draw.run()
      pygame.display.update()					#Atualização da tela
      self.clock.tick(FPS)					#Controle da taxa de quadros

if __name__ == '__main__':            		#Verificação se a biblioteca atual é a principal
  pendulo = Pendulo()                   			#Criação de uma instância de classe Pendulo
  pendulo.run()                         			#Chamada da função run (executar) dentro da classe Pendulo
