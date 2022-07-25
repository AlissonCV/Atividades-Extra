#!/usr/bin/python3

import pygame, sys						#Importação dos comandos dentro das bibliotecas pygame e sys (Sistema)
from settings import *						#Importaçao de todos os dados da biblioteca settings (configurações)
from button import Button					#Importação da classe Button da biblioteca button
from info import Info						#Importação da classe Info da biblioteca info
from draw import Draw						#Importação da classe Draw da biblioteca draw

class Pendulo:							#Definição de classe para chamadas
  def __init__(self):						#Definição de uma função de chamada incial
    #Configurações Gerais
    pygame.init()                                               #Inicialização da biblioteca pygame
    self.screen = pygame.display.set_mode((WIDTH,HEIGHT))	#Criação de uma superfície de exibição de acordo com as configurações de comprimento e tamanho
    pygame.display.set_caption('Inverted Pendulum Control')     #Alteração do título da janela
    self.clock = pygame.time.Clock()                            #Criação de um relógio
    #São configurações básicas necessarias para rodar a biblioteca pygame

    self.bg = pygame.image.load("Image/fundo.png")		#Variável para carregamento da tela de fundo
    self.play = Button(pygame.image.load("Image/quad1.png"), \
    (WIDTH/2, 250),"PLAY",get_font(75),"#d7fcd4","#0BCAFE")	#Variável para desenho do botão com o texto play
    self.info = Button(pygame.image.load("Image/quad1.png"), \
    (WIDTH/2, 400),"INFO",get_font(75),"#d7fcd4","#0BCAFE")	#Variável para desenho do botão com o texto info
    self.quit = Button(pygame.image.load("Image/quad1.png"), \
    (WIDTH/2, 550),"QUIT",get_font(75),"#d7fcd4","#0BCAFE")	#Variável para desenho do botão com o texto quit
    self.back = Button(None,(WIDTH*0.9, HEIGHT*0.8),"BACK", \
    get_font(40),"black","#0BCAFE")				#Variável para desenho do texto back
    self.Info = Info()						#Criação da chamada da classe Level
    self.draw = Draw()						#Criação da chamada da classe Level
    self.aux = True						#Variável auxiliara para controle do loop

  def run(self):						#Definição de uma função de execução
    while True:							#Criação de um loop infinito de verrificação
      self.screen.blit(self.bg,(0,0))				#Desenho da imagem da tela do fundo

      m_mouse_pos = pygame.mouse.get_pos()			#Criação de uma variável atribuindo a posição do mouse na tela

      m_text = get_font(90).render('AEROPÊNDULO',True, \
      '#041B04')						#Variável para desenho do titulo aeropendulo
      m_rect = m_text.get_rect(center = (WIDTH/2,100))		#Variável de posicionamento do titulo aeropendulo

      self.screen.blit(m_text,m_rect)				#Desenho do titulo aeropendulo

      for button in [self.play,self.info,self.quit]:		#Loop de verificação para mudança do estado do botão
        button.changeColor(m_mouse_pos)				#Chamada da função changeColor da classe Button para mudança da cor de acordo com a posição do mouse
        button.update(self.screen)				#Chamada da função update da classe Button para atualização do botão

      for event in pygame.event.get():				#Criação de uma verificação de eventos na tela pygame
        if event.type == pygame.QUIT:				#Verificando se o evento solicitado na tela pygame é de fechamento
          pygame.quit()						#Fechamento da tela pygame
          sys.exit()						#Fechamento da execução
        if event.type == pygame.MOUSEBUTTONDOWN:		#Verificação se o botão do mouse foi clicado
          if self.play.checkForInput(m_mouse_pos):		#Verificação se a posição do mouse é a mesma do botão play
            i = 0						#Definição da Variável para leitura da matrix de ângulos
            aux1 = 0						#Definição da Variável auxiliar para delay de entrada de tela
            while self.aux:					#Inicio de loop para plotagem do movimento do pendulo
              i_mouse_pos = pygame.mouse.get_pos()		#Criação de uma variável atribuindo a posição do mouse na tela
              self.screen.fill('white')				#Preenchimento da tela com a cor branca
              i = self.draw.run(i)				#Chamada da função run (executar) da classe Level e atribui o retorno da chamada na variável i

              self.back.changeColor(i_mouse_pos)		#Chamada da função changeColor da classe Button para mudança da cor de acordo com a posição do mouse
              self.back.update(self.screen)			#Chamada da função update da classe Button para atualização do botão

              for event1 in pygame.event.get():			#Criação de uma verificação de eventos na tela pygame
                if event1.type == pygame.QUIT:			#Verificando se o evento solicitado na tela pygame é de fechamento
                  pygame.quit()					#Fechamento da tela pygame
                  sys.exit()					#Fechamento da execução
                if event1.type == pygame.MOUSEBUTTONDOWN:	#Verificação se o botão do mouse foi clicado
                  if self.back.checkForInput(i_mouse_pos):	#Verificação se a posição do mouse é a mesma do botão back
                    self.aux = False				#Mudança da variável auxiliar para saída do loop

              pygame.display.update()				#Atualização da tela

              if aux1 == 0:					#Verificação do valor da variável auxiliar
                aux1 = 1					#Mudança da variável auxiliar para não realizar mais a função delay
                pygame.time.delay(300)				#Delay para visualização do início

              self.clock.tick(0.1*FPS)				#Controle da taxa de quadros
            self.aux = True					#Mudança da variável auxiliar para novos eventos de loop
          if self.info.checkForInput(m_mouse_pos):		#Verificação se a posição do mouse é a mesma do botão back#Verificação se o clique do mouse foi no botão info
            while self.aux:					#Inicio de loop para plotagem das informações do projeto
              i_mouse_pos = pygame.mouse.get_pos()		#Criação de uma variável atribuindo a posição do mouse na tela

              self.Info.info()					#Chamada da função info da classe Level

              self.back.changeColor(i_mouse_pos)		#Chamada da função changeColor da classe Button para mudança da cor de acordo com a posição do mouse
              self.back.update(self.screen)			#Chamada da função update da classe Button para atualização do botão

              for event1 in pygame.event.get():			#Criação de uma verificação de eventos na tela pygame
                if event1.type == pygame.QUIT:			#Verificando se o evento solicitado na tela pygame é de fechamento
                  pygame.quit()					#Fechamento da tela pygame
                  sys.exit()					#Fechamento da execução
                if event1.type == pygame.MOUSEBUTTONDOWN:	#Verificação se o botão do mouse foi clicado
                  if self.back.checkForInput(i_mouse_pos):	#Verificação se a posição do mouse é a mesma do botão back
                    self.aux = False				#Mudança da variável auxiliar para saída do loop

              pygame.display.update()				#Atualização da tela
            self.aux = True					#Mudança da variável auxiliar para novos eventos de loop
          if self.quit.checkForInput(m_mouse_pos):		#Verificação se a posição do mouse é a mesma do botão quit
            pygame.quit()					#Fechamento da tela pygame
            sys.exit()						#Fechamento da execução

      pygame.display.update()					#Atualização da tela

#Definição da Fonte
def get_font(size):								#Definição de uma função para chamada de mudança de fonte
  return pygame.font.Font("Font/font.ttf", size)				#Retorna o valor as predefinições do tamanho e o tipo de fonte

if __name__ == '__main__':            				#Verificação se a biblioteca atual é a principal
  pendulo = Pendulo()                   			#Criação de uma instância de classe Pendulo
  pendulo.run()                         			#Chamada da função run (executar) dentro da classe Pendulo
