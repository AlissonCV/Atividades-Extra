#!/usr/bin/python3
#Configurações do objeto jogador do jogo

import pygame #Importação dos comandos dentro da biblioteca pygame
from settings import * #Importação de todos os comandos de configurações
from suporte import import_folder
from entity import Entity

class Player(Entity):
  def __init__(self,pos,groups,obstacle_sprites,create_attack,destroy_attack,create_magic):
    super().__init__(groups)
    self.image = pygame.image.load('graphics/test/player.png').convert_alpha()
    self.rect = self.image.get_rect(topleft = pos)
    self.hitbox = self.rect.inflate(0,-26)

    #setup dos gráficos
    self.import_player_assets()
    self.status = 'down'
    #self.frame_index = 0
    #self.animation_speed = 0.15

    #define os controles para ataque e magia
    #self.direction = pygame.math.Vector2()
    self.attacking = False # usado para criar um timer de ataque
    self.attack_cooldown = 400 #define um tempo intervalo de ataque
    self.attack_time = None #variável para armazenar o tempo de ataque
    self.obstacle_sprites = obstacle_sprites

    # Define os controles para ataque
    self.create_attack = create_attack
    self.destroy_attack = destroy_attack
    self.weapon_index = 0 #define o índice inicial da arma a ser usada
    self.weapon = list(weapon_data.keys())[self.weapon_index] #seleciona a arma do jogador
    self.can_switch_weapon = True #flag para verificar se pode trocar a arma
    self.weapon_switch_time = None #variável para armazenar o tempo de troca das armas
    self.switch_duration_cooldown = 200 #define um tempo intervalo de troca de arma

    # Define os controles para as magias
    self.create_magic = create_magic
    self.magic_index = 0 #define o índice inicial da magia a ser usada
    self.magic = list(magic_data.keys())[self.magic_index] #seleciona a magia do jogador
    self.can_switch_magic = True #flag para verificar se pode trocar a magia
    self.magic_switch_time = None #variável para armazenar o tempo de troca das magias

    # Define os parâmetros dos status do jogo
    self.stats = {'health': 100, 'energy': 60, 'attack': 10, 'magic': 4, 'speed': 5} #estatisticas dos parametros que o jogador possui inicialmente
    self.max_stats = {'health': 300, 'energy': 140, 'attack': 20, 'magic': 10, 'speed': 10} #estatisticas dos parametros que o jogador pode ter como máximo
    self.upgrade_cost = {'health': 100, 'energy': 100, 'attack': 100, 'magic': 100, 'speed': 100}
    self.health = self.stats['health'] * 0.5 #define a vida do jogador como 50% do padrão
    self.energy = self.stats['energy'] * 0.8 #define a energia do jogador como 80% do padrão
    self.exp = 5000 #define a experiência do jogador inicial
    self.speed = self.stats['speed'] #define a velociade inicial

    # damage timer
    self.vulnerable = True
    self.hurt_time = None
    self.invulnerability_duration = 500

    # import a sound
    #self.weapon_attack_sound = pygame.mixer.Sound('../audio/sword.wav')
    #self.weapon_attack_sound.set_volume(0.4)

  def import_player_assets(self): #importa as posições das animações do icone do jogador
    character_path = 'graphics/player/'
    # diferentes estados em que o icone do jogador está
    self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                       'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
                       'right_attack': [], 'left_attack': [], 'up_attack': [], 'down_attack': []}

    for animation in self.animations.keys(): #dentre a lista de animações pega o nome do arquivo correspondente
      full_path = character_path + animation
      self.animations[animation] = import_folder(full_path)

  def input(self):
    if not self.attacking: #se o jogador estiver atacando não faz mais nenhum movimento
      keys = pygame.key.get_pressed()

      #entradas de movimentos
      if keys[pygame.K_UP]: #seta para cima decrementa a posição y
        self.direction.y = -1
        self.status = 'up'
      elif keys[pygame.K_DOWN]: #seta para baixo incrementa a posição y
        self.direction.y = 1
        self.status = 'down'
      else:
        self.direction.y = 0

      if keys[pygame.K_RIGHT]: #seta para direita incrementa a posição x
        self.direction.x = 1
        self.status = 'right'
      elif keys[pygame.K_LEFT]: #seta para esquerda decrementa a posição x
        self.direction.x = -1
        self.status = 'left'
      else:
        self.direction.x = 0

      #entradas de ataques
      if keys[pygame.K_SPACE]: #tecla barra de espaço faz um ataque
        self.attacking = True
        self.attack_time = pygame.time.get_ticks()
        self.create_attack()
#        self.weapon_attack_sound.play()

      #entradas de magias
      if keys[pygame.K_LCTRL]: #tecla CTRL faz o ataque de magia
        self.attacking = True #define o flag de ataque como True
        self.attack_time = pygame.time.get_ticks() #pega o tempo do sistema em que foi feito o ataque
        style = list(magic_data.keys())[self.magic_index] #define a variável style com os parâmetros da magia do jogador ativa, da base de dados magic_data
        strength = list(magic_data.values())[self.magic_index]['strength'] + self.stats['magic'] #armazena a força da magia usada adicionando a magia existente da variável stats
        cost = list(magic_data.values())[self.magic_index]['cost'] #cria uma variavel para armazenar o custo da magia
        self.create_magic(style, strength, cost) #chama a função para cria a magia

      #tecla q troca a arma
      if keys[pygame.K_q] and self.can_switch_weapon: #se selecionado a tecla para trocar a arma e o flag para troca da arma estiver ativo
        self.can_switch_weapon = False #seta o flag de troca de arma para false
        self.weapon_switch_time = pygame.time.get_ticks() #pega o horário que foi precionado a tecla de troca de arma

        if self.weapon_index < len(list(weapon_data.keys())) - 1: #se chegar ao fim da lista volta ao inicio, ou incrementa o indice da arma
          self.weapon_index += 1 #incrementa o indice da arma
        else:
          self.weapon_index = 0 #zera o indice da arma

        self.weapon = list(weapon_data.keys())[self.weapon_index] #pega os dados da arma da base de dados weapon_data

      # tecla e troca a magia
      if keys[pygame.K_e] and self.can_switch_magic: #comentários semelhante ao da arma, trocando para magia
        self.can_switch_magic = False
        self.magic_switch_time = pygame.time.get_ticks()

        if self.magic_index < len(list(magic_data.keys())) - 1:
          self.magic_index += 1
        else:
          self.magic_index = 0

        self.magic = list(magic_data.keys())[self.magic_index]

  def get_status(self):
    # status parado
    if self.direction.x == 0 and self.direction.y == 0: #verifica se o jogador está parado
      if not 'idle' in self.status and not 'attack' in self.status: #se o status não possuir a flag _idle coloca _idle para indicar parado
        self.status = self.status + '_idle' #coloca um _idle e parado no último movimento que fez antes

    if self.attacking: #verifica se o status é de atacando ou fazendo mágica
      self.direction.x = 0 #faz com que não ocorra ataque e movimento ao mesmo tempo
      self.direction.y = 0 #faz com que não ocorra ataque e movimento ao mesmo tempo
      if not 'attack' in self.status: #se não houver ataque no status do personagem
        if 'idle' in self.status: #verifica se já existe o flag _idle no status
          self.status = self.status.replace('_idle', '_attack') #se tiver o flag de _idle, troca para ataque pois estava parado e está atacando
        else:
          self.status = self.status + '_attack' #coloca o status como ataque
    else:
      if 'attack' in self.status: #verifica se existe o flag attack no status
        self.status = self.status.replace('_attack', '') #caso tenha retira do status

  def colldowns(self): #define uma função de delay do ataque e mágica
    current_time = pygame.time.get_ticks()
    if self.attacking: #verifica se o flag de controle dos ataques e magias foram ativados = true
      if current_time - self.attack_time >= self.attack_cooldown: #verifica se o tempo entre o ataque e o tempo do sistema é igual ao tempo de espera
        self.attacking = False #define o flag para não ocorrencia de ataque ou magia
        self.destroy_attack() #após passar o tempo do ataque, destroi a arma
    if not self.can_switch_weapon: #verifica se o flag da troca de armas esta falso
      if current_time-self.weapon_switch_time >= self.switch_duration_cooldown: #após passar o tempo da troca da arma seta o flag para verdadeiro
        self.can_switch_weapon = True
    if not self.can_switch_magic: #verifica se o flag da troca de magias esta falso
      if current_time-self.magic_switch_time >= self.switch_duration_cooldown: #após passar o tempo da troca da magia seta o flag para verdadeiro
        self.can_switch_magic = True

  def animate(self): #define a animação para o jogador para cada movimento
    anima_aux = self.animations[self.status] #pega um dos status da lista de animações

    # faz um loop dos índices do frame do jogador na velocidade definida
    self.frame_index += self.animation_speed
    if self.frame_index >= len(anima_aux): #se chegar ao fim do indice das animações existentes volta para a primeira
      self.frame_index = 0

    # define a imagem correspondente a cada frame a ser mostrado para o jogador
    self.image = anima_aux[int(self.frame_index)]
    self.rect = self.image.get_rect(center=self.hitbox.center) #redefine o retangulo da imagem do jogador, para adaptar a tamanhos diferentes

    # flicker
    if not self.vulnerable:
      alpha = self.wave_value()
      self.image.set_alpha(alpha)
    else:
      self.image.set_alpha(255)

  def get_full_weapon_damage(self):
    base_damage = self.stats['attack']
    weapon_damage = weapon_data[self.weapon]['damage']
    return base_damage + weapon_damage

  def get_full_magic_damage(self):
    base_damage = self.stats['magic']
    spell_damage = magic_data[self.magic]['strength']
    return base_damage + spell_damage

  def get_value_by_index(self, index):
    return list(self.stats.values())[index]

  def get_cost_by_index(self, index):
    return list(self.upgrade_cost.values())[index]

  def energy_recovery(self):
    if self.energy < self.stats['energy']:
      self.energy += 0.01 * self.stats['magic']
    else:
      self.energy = self.stats['energy']

  def update(self):
    self.input()
    self.colldowns()
    self.get_status()
    self.animate()
    self.move(self.stats['speed'])
    self.energy_recovery()
