#!/usr/bin/python3

import pygame, sys					  #Importação dos comandos dentro das bibliotecas pygame e sys (Sistema)
from settings import *					  #Importação de todos os dados da biblioteca settings (configurações)
from level import Level					  #Importação da classe Level da biblioteca level

class Game:						  #Definição de classe para chamadas
  def __init__(self):					  #Definição de uma função de chamada inicial
    #Configurações Gerais
    pygame.init()					  #Inicialização da biblioteca pygame
    self.screen = pygame.display.set_mode((WIDTH,HEIGHT)) #Criação de uma superfície de exibição de acordo com as configurações de comprimento e tamanho
    pygame.display.set_caption('Zelda')			  #Alteração do título da janela
    self.clock = pygame.time.Clock()			  #Criação de um relógio
    #São configurações básicas necessarias para rodar a biblioteca pygame

    self.level = Level()				  #Criação da chamada da clase Level

  def run(self):					  #Definição de uma função de execução
    while True:						  #Criação de um loop infinito de verificação
      for event in pygame.event.get():			  #Criação de uma verificação de eventos dentro do jogo
        if event.type == pygame.QUIT:			  #Verificando se o evento solicitado no jogo é de fechamento do jogo
          pygame.quit()					  #Fechamento do jogo
          sys.exit()					  #Fechamento da execução

      self.screen.fill('black')				  #Preenchimento da tela com a cor preta
      self.level.run()					  #Chamada da função run (executar) da classe Level
      pygame.display.update()				  #Atualização da tela
      self.clock.tick(FPS)				  #Controle da taxa de quadros

if __name__ == '__main__':				  #Verificação se a biblioteca atual é a principal
  game = Game()						  #Criação de uma instância da classe do jogo
  game.run()						  #Chamada da função de execução dentro da classe jogo
