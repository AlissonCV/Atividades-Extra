#!/usr/bin/activate

import pygame
import sys
from button import Button
from settings import *

class Teste:
  def __init__(self):
    #Pega as informações da superficie
    self.display_surface = pygame.display.get_surface()	#Capturando a superfície da tela pygame aberta

    # basic font for user typed
    self.base_font = pygame.font.Font(None, 32)
    self.user_text = ''

    # create rectangle
    self.input_rect = pygame.Rect(10, 10, 35, 32)

    # color_active stores color(lightskyblue3) which gets active when input box is clicked by user
    self.color_active = pygame.Color('lightskyblue3')

    # color_passive store color(chartreuse4) which is color of input box.
    self.color_passive = pygame.Color('gray')
    self.color = self.color_passive

    self.active = False
    self.aux = True

    self.back = Button(None,(WIDTH*0.9, HEIGHT*0.8),"BACK", \
    get_font(40),"black","#0BCAFE")

  def entrada(self, count, w):
    if count == 0:
      while self.aux:
        i_mouse_pos = pygame.mouse.get_pos()

        self.back.changeColor(i_mouse_pos)                #Chamada da função changeColor da classe Button para mudança da cor de acordo com a posição do mouse
        self.back.update(self.display_surface)

        for event in pygame.event.get():
          # if user types QUIT then the screen will close
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

          if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back.checkForInput(event.pos):
              self.aux = False
              w = False

            if self.input_rect.collidepoint(event.pos):
              self.active = True
            else:
              self.active = False

          if event.type == pygame.KEYDOWN and self.active:
            # Check for backspace
            if event.key == pygame.K_KP_ENTER:
              self.aux = False

            # Unicode standard is used for string formation
            else:
              self.user_text += event.unicode

        if self.active:
          self.color = self.color_active
        else:
          self.color = self.color_passive

        # draw rectangle and argument passed which should be on screen
        pygame.draw.rect(self.display_surface, self.color, self.input_rect)

        text_surface = self.base_font.render(self.user_text, True, 'white')

        # render at position stated in arguments
        self.display_surface.blit(text_surface, (self.input_rect.x+5, self.input_rect.y+5))

        # display.flip() will update only a portion of the screen to updated, not full area
        pygame.display.update()

      self.aux = True
      count = 1
      return self.user_text, count, w
    else:
      for event in pygame.event.get():
        # if user types QUIT then the screen will close
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

      self.color = self.color_passive

      # draw rectangle and argument passed which should be on screen
      pygame.draw.rect(self.display_surface, self.color, self.input_rect)

      text_surface = self.base_font.render(self.user_text, True, 'black')

      # render at position stated in arguments
      self.display_surface.blit(text_surface, (self.input_rect.x+5, self.input_rect.y+5))

    return self.user_text, count

def get_font(size):
  return pygame.font.Font("Font/font.ttf", size)
