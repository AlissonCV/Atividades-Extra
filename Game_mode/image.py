#!/usr/bin/python3

import pygame

class Image(pygame.sprite.Sprite):
  def __init__(self, pos1, pos2, groups):
    super().__init__(groups)
    self.haste = pygame.image.load('Imagem/haste.png')
    self.rect1 = pygame.image.get_rect(center = pos1)
    self.apoio = pygame.image.load('Imagem/fixacao.png')
    self.rect2 = pygame.image.get_rect(top = pos1)
    self.motor = pygame.image.load('Imagem/motor.png')
    self.rect3 = pygame.image.get_rect(center = pos2)

  def move(self):
    self.rect2.top = pos1
    self.rect2.bottom = pos2
    self.rect3.center = pos2
