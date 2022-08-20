#!/usr/bin/python3

import pygame, sys						#Importação dos comandos dentro das bibliotecas pygame e sys (Sistema)
from settings import *						#Importaçao de todos os dados da biblioteca settings (configurações)
from level import Level						#Importação da classe Level da biblioteca level

class Pendulo:							#Definição de classe para chamadas
  def __init__(self):						#Definição de uma função de chamada incial
    #Configurações Gerais
    pygame.init()                                               #Inicialização da biblioteca pygame
    self.screen = pygame.display.set_mode((WIDTH,HEIGHT))	#Criação de uma superfície de exibição de acordo com as configurações de comprimento e tamanho
    pygame.display.set_caption('Inverted Pendulum Control')     #Alteração do título da janela
    self.clock = pygame.time.Clock()                            #Criação de um relógio
    #São configurações básicas necessarias para rodar a biblioteca pygame

    self.level = Level()					#Criação da chamada da classe Level

  def run(self):						#Definição de uma função de execução
    while True:							#Criação de um loop infinito de verrificação
      for event in pygame.event.get():				#Criação de uma verificação de eventos na tela pygame
        if event.type == pygame.QUIT:				#Verificando se o evento solicitado na tela pygame é de fechamento
          pygame.quit()						#Fechamento da tela pygame
          sys.exit()						#Fechamento da execução

      self.screen.fill('white')                           	#Preenchimento da tela com a cor branca
      self.level.run()						#Chamada da função run (executar) da classe Level
      pygame.display.update()					#Atualização da tela
      self.clock.tick(FPS)					#Controle da taxa de quadros

if __name__ == '__main__':            				#Verificação se a biblioteca atual é a principal
  pendulo = Pendulo()                   			#Criação de uma instância de classe Pendulo
  pendulo.run()                         			#Chamada da função run (executar) dentro da classe Pendulo
