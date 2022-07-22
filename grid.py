#!/usr/bin/python3

import pygame
from settings import *

class Grid:
  def __init__(self):
    self.display_surface = pygame.display.get_surface()

  def run(self):
    for x in range(25,WIDTH,25):
      pygame.draw.lines(self.display_surface,'gray',False,[(x,0),(x,HEIGHT)])
    for y in range(25,HEIGHT,25):
      pygame.draw.lines(self.display_surface,'gray',False,[(0,y),(WIDTH,y)])
