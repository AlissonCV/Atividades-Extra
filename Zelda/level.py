#!/usr/bin/python3

import pygame										#
from settings import *									#
from tile import Tile									#
from player import Player								#

class Level:										#
  def __init__(self):									#
    #Pega as informações da superfície
    self.display_surface = pygame.display.get_surface()					#

    #Grupo de configurações de sprite
    self.visible_sprites = YSortCameraGroup()					#
    self.obstacle_sprites = pygame.sprite.Group()					#

    #Configurações de sprite
    self.create_map()									#

  def create_map(self):									#
    for row_index, row in enumerate(WORLD_MAP):						#
      for col_index, col in enumerate(row):						#
        #print(row_index)
        #print(row)
        #print(col_index)
        x = col_index * TILESIZE							#
        y = row_index * TILESIZE							#

        if col == 'x':									#
          Tile((x,y),[self.visible_sprites,self.obstacle_sprites])			#
        if col == 'p':
          self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)	#

  def run(self):									#
    #Atualização e desenhar o jogo
    self.visible_sprites.custom_draw(self.player)							#
    self.visible_sprites.update()							#

class YSortCameraGroup(pygame.sprite.Group):
  def __init__(self):
    #Configurações Gerais
    super().__init__()
    self.display_surface = pygame.display.get_surface()
    self.half_width = self.display_surface.get_size()[0] // 2
    self.half_height = self.display_surface.get_size()[1] // 2
    self.offset = pygame.math.Vector2()

  def custom_draw(self,player):
    #Obtendo o offset
    self.offset.x = player.rect.centerx - self.half_width
    self.offset.y = player.rect.centery - self.half_height

    for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
      offset_pos = sprite.rect.topleft - self.offset
      self.display_surface.blit(sprite.image,offset_pos)
