#!/usr/bin/python3
#configura os níveis do jogo
import pygame #Importação dos comandos dentro da biblioteca pygame
from settings import * #Importação de todos os comandos de configurações
from tile import Tile #importação do módulo tile.py
from player import Player #importação do módulo tile.py
from suporte import * #importa as configurações de suporte para leitura do arquivo CSV como o mapa
from random import choice,randint #importa o método choice e randint do módulo random
from weapon import Weapon #importa a classe Weapon do weapon.py
from ui import UI #importa a função de Interface de Usuário do jogo do módulo ui.py
from enemy import Enemy
from particles import AnimationPlayer
from magic import MagicPlayer
from upgrade import Upgrade

class Level: #Define uma classe para configurar os níveis do jogo
  def __init__(self):
    # define uma variável para armazerar a superfície de display do gráfico do jogo
    self.display_surface = pygame.display.get_surface()	#Pega uma referência da superfície de exibição atualmente definida
    self.game_paused = False

    #Grupo de configurações de sprite
    self.visible_sprites = YSortCameraGroup() #define a função para ordenar as cameras
    self.obstacle_sprites = pygame.sprite.Group() #defiine a função para configurar os obstaculos

    #Sprites de ataque
    self.current_attack = None #define variavel do ataque corrente
    self.attack_sprites = pygame.sprite.Group()
    self.attackable_sprites = pygame.sprite.Group()

    #Configurações de sprite
    self.create_map() #define a função de criar o mapa

    #Interface de usuários
    self.ui = UI()
    self.upgrade = Upgrade(self.player)

    # particles
    self.animation_player = AnimationPlayer()
    self.magic_player = MagicPlayer(self.animation_player)

  def create_map(self): #função para configurar o mapa
    layouts = { #ao invés usar o mapa de WORLD_MAP, lê o arquivo .csv das rochas/tijolos, lê o arquivo .csv da grama e .csv dos objetos
      'boundary': import_csv_layout('graphics/map/map_FloorBlocks.csv'),
      'grass': import_csv_layout('graphics/map/map_Grass.csv'),
      'object': import_csv_layout('graphics/map/map_Objects.csv'),
      'entities': import_csv_layout('graphics/map/map_Entities.csv')
    }
    graphics = {
      'grass': import_folder('graphics/grass'),
      'objects': import_folder('graphics/objects')
    }
    for style,layout in layouts.items():
      for row_index, row in enumerate(layout):	#enumera a matríz retornando o índice das linhas e as linhas
        for col_index, col in enumerate(row):	##enumera a linha retornando o índice das colunas
          #pega somente os valores não negativos do arquivo csv
          if col != '-1':
            x = col_index * TILESIZE # multiplica os índices das colunas pelo tamanho do ladrilho
            y = row_index * TILESIZE # multiplica os índices das linhas pelo tamanho do ladrilho
            if style == 'boundary':
              Tile((x,y),[self.obstacle_sprites],'invisible')

            if style == 'grass':
              random_grass_image = choice(graphics['grass']) #escolhe randomicamente uma arbusto das constantes na lista importada
              Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'grass',random_grass_image) #desenha os arbustos

            if style == 'object':
              surf = graphics['objects'][int(col)] #pega o index das colunas para definir a superfície
              Tile((x,y,),[self.visible_sprites,self.obstacle_sprites],'object',surf) #desenha os objetos da superficie

            if style == 'entities':
              if col == '394':
                self.player = Player(
                  (x, y),
                  [self.visible_sprites],
                  self.obstacle_sprites,
                  self.create_attack,
                  self.destroy_attack,
                  self.create_magic) #coloca o jogador no mapa
              else:
                if col == '390':
                  monster_name = 'bamboo'
                elif col == '391':
                  monster_name = 'spirit'
                elif col == '392':
                  monster_name = 'raccoon'
                else:
                  monster_name = 'squid'
                Enemy(
                  monster_name,
                  (x, y),
                  [self.visible_sprites, self.attackable_sprites],
                  self.obstacle_sprites,
                  self.damage_player,
                  self.trigger_death_particles,
                  self.add_exp) #coloca o inimigo no mapa

  def create_attack(self):
    self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])

  def create_magic(self,style,strenght,cost):
    if style == 'heal':
      self.magic_player.heal(self.player, strength, cost, [self.visible_sprites])

    if style == 'flame':
      self.magic_player.flame(self.player, cost, [self.visible_sprites, self.attack_sprites])

  def destroy_attack(self):
    if self.current_attack: #verifica se existe algum ataque destroi
      self.current_attack.kill()
    self.current_attack = None

  def player_attack_logic(self):
    if self.attack_sprites:
      for attack_sprite in self.attack_sprites:
        collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
        if collision_sprites:
          for target_sprite in collision_sprites:
            if target_sprite.sprite_type == 'grass':
              pos = target_sprite.rect.center
              offset = pygame.math.Vector2(0, 75)
              for leaf in range(randint(3, 6)):
                self.animation_player.create_grass_particles(pos - offset, [self.visible_sprites])
              target_sprite.kill()
            else:
              target_sprite.get_damage(self.player, attack_sprite.sprite_type)

  def damage_player(self, amount, attack_type):
    if self.player.vulnerable:
      self.player.health -= amount
      self.player.vulnerable = False
      self.player.hurt_time = pygame.time.get_ticks()
      self.animation_player.create_particles(attack_type, self.player.rect.center, [self.visible_sprites])

  def trigger_death_particles(self, pos, particle_type):
    self.animation_player.create_particles(particle_type, pos, self.visible_sprites)

  def add_exp(self, amount):
    self.player.exp += amount

  def toggle_menu(self):
    self.game_paused = not self.game_paused

  def run(self): #define uma função para executar a atualização do desenho
    #Atualização e desenhar o jogo
    self.visible_sprites.custom_draw(self.player) #Desenha o jogador de forma customizada
    self.ui.display(self.player)

    if self.game_paused:
      self.upgrade.display()  # Atualiza o desenho
    else:
      self.visible_sprites.update()
      self.visible_sprites.enemy_update(self.player)
      self.player_attack_logic()


class YSortCameraGroup(pygame.sprite.Group):
  def __init__(self):
    #Configurações Gerais
    super().__init__()
    self.display_surface = pygame.display.get_surface()
    self.half_width = self.display_surface.get_size()[0] // 2
    self.half_height = self.display_surface.get_size()[1] // 2
    self.offset = pygame.math.Vector2()

    # Cria a variável superfície para a imagem do solo do mapa e cria a
    self.floor_surf = pygame.image.load('graphics/tilemap/ground.png').convert()
    self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0)) #cria uma tupla com as corrdenadas 0,0,tamnaho da imagem(x,y)

  # aplica offset nos objetos e desenha
  def custom_draw(self,player):
    #Obtendo o offset
    self.offset.x = player.rect.centerx - self.half_width
    self.offset.y = player.rect.centery - self.half_height

    # desenha o solo do mapa no offset da camera
    floor_offset_pos = self.floor_rect.topleft - self.offset
    self.display_surface.blit(self.floor_surf, floor_offset_pos)

    # faz um loop dos sprites que estão no self.sprites():
    for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
      offset_pos = sprite.rect.topleft - self.offset
      self.display_surface.blit(sprite.image,offset_pos)

  def enemy_update(self,player):
    enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
    for enemy in enemy_sprites:
      enemy.enemy_update(player)