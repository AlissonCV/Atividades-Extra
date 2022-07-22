#!/usr/bin/python3

import pygame						#Importação dos comandos dentro da biblioteca pygame

pygame.init()						#
fonte = pygame.font.Font(None,30)			#Definição de uma variável com as especificações da fonte

def debug(info,y = 10, x = 10):				#Definição de uma função de debug (depuração)
  display_surface = pygame.display.get_surface()	#Definição de uma variável de obtenção da superfície do jogo
  debug_surf = fonte.render(str(info),True,'White')	#Definição de uma variável de renderização do texto
  debug_rect = debug_surf.get_rect(topleft = (x,y))	#Definição de uma variável de posicionamento do texto
  pygame.draw.rect(display_surface,'Black',debug_rect)	#Chamada para desenho do texto na tela
  display_surface.blit(debug_surf,debug_rect)		#
