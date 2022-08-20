#!/usr/bin/python3

import pygame, sys
from settings import *

class Info():
  def __init__(self):
    #Pega as informações da superficie
    self.screen = pygame.display.get_surface()       #Criação de uma superfície de exibição de acordo com as configurações de comprimento e tamanho

  #Entrada de dados do tipo de fonte e da posição onde será colocado o texto
  def info(self):
      self.screen.fill("white")
      i_text = get_font(18).render("Sistemas Embarcados II - Trabalho Prático 01: Sistema de Controle", True, "Black")
      i_rect = i_text.get_rect(center=(WIDTH/2, 70))
      self.screen.blit(i_text, i_rect)
      i_text = get_font(17).render("PROFESSOR: Éder Alves de Moura", True, "Black")
      i_rect = i_text.get_rect(center=(WIDTH/2, 120))
      self.screen.blit(i_text, i_rect)
      i_text = get_font(17).render("GRUPO: ", True, "Black")
      i_rect = i_text.get_rect(center=(WIDTH/2, 170))
      self.screen.blit(i_text, i_rect)
      i_text = get_font(17).render("Alisson Carvalho Vasconcelos     -11511EMT016", True, "Black")
      i_rect = i_text.get_rect(center=(WIDTH/2, 210))
      self.screen.blit(i_text, i_rect)
      i_text = get_font(17).render("André de Oliveira Águila Favotto - 11811EAU013", True, "Black")
      i_rect = i_text.get_rect(center=(WIDTH/2, 250))
      self.screen.blit(i_text, i_rect)
      i_text = get_font(17).render("Gabriel Medeiros Sollero         - 11811EAU000", True, "Black")
      i_rect = i_text.get_rect(center=(WIDTH/2, 290))
      self.screen.blit(i_text, i_rect)
      i_text = get_font(17).render("João Victor Luiz de Andrade      - 11811EAU003", True, "Black")
      i_rect = i_text.get_rect(center=(WIDTH/2, 330))
      self.screen.blit(i_text, i_rect)
      i_text = get_font(17).render("Rodrigo Santana Soares           - 11821EAU013", True, "Black")
      i_rect = i_text.get_rect(center=(WIDTH/2, 370))
      self.screen.blit(i_text, i_rect)
      i_text = get_font(17).render("Thiago Fernando Cuevas Mestanza  - 11821EAU002", True, "Black")
      i_rect = i_text.get_rect(center=(WIDTH/2, 410))
      self.screen.blit(i_text, i_rect)

#Definição da Fonte
def get_font(size):								#Definição de uma função para chamada de mudança de fonte
  return pygame.font.Font("Font/font.ttf", size)				#Retorna o valor as predefinições do tamanho e o tipo de fonte
