#!/usr/bin/python3

import pygame
from settings import *
from simulacao_pendulo import simulacao

class Draw:
  def __init__(self):
    self.display_surface = pygame.display.get_surface()

    self.x = XY[0]
    self.y = XY[1]
    self.radius = 20

  def run(self):
    pass
#    pygame.draw.circle(self.display_surface,'black',(WIDTH/2, 100),4)
#    pygame.draw.line(self.display_surface,'black',[(WIDTH/2, 100),(self.x, self.y)],2)
#    pygame.draw.circle(self.display_surface,'black',(self.x, self.y),self.radius)
#    pygame.draw.circle(self.display_surface,'red',(self.x, self.y),self.radius-2)
