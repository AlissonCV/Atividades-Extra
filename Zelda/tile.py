#!/usr/bin/python3
#Configuração dos Objeto Rochas/Tijolos, grama, obstaculos do jogo

import pygame #Importação dos comandos dentro da biblioteca pygame
from settings import * #Importação de todos os comandos de configurações

class Tile(pygame.sprite.Sprite):
  def __init__(self,pos,groups,sprite_type, surface = pygame.Surface((TILESIZE,TILESIZE))):
    super().__init__(groups)
    self.sprite_type = sprite_type
    self.image = surface #pygame.image.load('graphics/test/rock.png').convert_alpha()
    if sprite_type == 'object':
      self.rect = self.image.get_rect(topleft=(pos[0],pos[1] - TILESIZE)) #como existem alguns objetos maiores que a grama, altera a posição de sobreposição para TILESIZE acima
    else:
      self.rect = self.image.get_rect(topleft = pos)
    self.hitbox = self.rect.inflate(0,-10)
