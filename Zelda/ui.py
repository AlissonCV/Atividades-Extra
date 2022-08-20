import pygame #Importação dos comandos dentro da biblioteca pygame
from settings import * #Importação de todos os comandos de configurações

class UI:
	def __init__(self):
		
		# Define os parâmetros gerais da Interface de Usuários
		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)

		# Define os parâmetros da barra de setup
		self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT) #define a variável da barra de vida
		self.energy_bar_rect = pygame.Rect(10,34,ENERGY_BAR_WIDTH,BAR_HEIGHT) #define a variável da barra de energia

		# Converte o dicionário de armas existentes no jogo para uma variável do tamanho das superfícies das armas
		self.weapon_graphics = [] #define a variável que armazena de graficos das armas
		for weapon in weapon_data.values(): #faz um loop entre as armas definidas na variável weapon_data
			path = weapon['graphic'] #pega o caminho de onde estão as imagens das armas no item graphics
			weapon = pygame.image.load(path).convert_alpha() #lê o arquivo da imagem das armas
			self.weapon_graphics.append(weapon) #armazena a imagem na lista de armas

		# Converte o dicionário de magias existentes no jogo para uma variável do tamanho das superfícies das armas
		self.magic_graphics = [] #define a variável que armazena de graficos das magias
		for magic in magic_data.values(): #faz um loop entre as magias definidas na variável magic_data
			path = magic['graphic'] #pega o caminho de onde estão as imagens das magias no item graphics
			magic = pygame.image.load(path).convert_alpha() #lê o arquivo da imagem das magias
			self.magic_graphics.append(magic) #armazena a imagem na lista de magias

	def show_bar(self,current,max_amount,bg_rect,color): #função para mostrar a barra de status
		# desenha a tela de fundo da vida ou energia do jogador
		pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)

		# converte status em pixeis para mostrar o nivel de energia ou vida do jogador
		ratio = current / max_amount
		current_width = bg_rect.width * ratio
		current_rect = bg_rect.copy()
		current_rect.width = current_width

		# Desenha a barra de vida ou energia que o jogador tem
		pygame.draw.rect(self.display_surface,color,current_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)

	def show_exp(self,exp): #define uma função para mostrar a experiência do jogador no canto direito inferior da tela
		text_surf = self.font.render(str(int(exp)),False,TEXT_COLOR)
		x = self.display_surface.get_size()[0] - 20 #defina a coordenada x = dimensão da tela em x - 20 pixels
		y = self.display_surface.get_size()[1] - 20 #defina a coordenada y = dimensão da tela em y - 20 pixels
		text_rect = text_surf.get_rect(bottomright = (x,y)) #define um retangulo nas dimensões do texto considerando a coordenada inferior direita do retangulo do texto como x,y

		pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(20,20)) #desenha um retangulo aumentado de 20 que ficará embaixo do texto
		self.display_surface.blit(text_surf,text_rect) #desenha o texto no gráfico da janela
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),3) #desenha um frame/borda em volta do retangulo

	def selection_box(self,left,top, has_switched): #cria uma função para as armas e magias selecionadas
		bg_rect = pygame.Rect(left,top,ITEM_BOX_SIZE,ITEM_BOX_SIZE) #define uma variável do retangulo de fundo dos objetos selecionados
		pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect) #desenha o retangulo de fundo no grafico da janela
		if has_switched:
			pygame.draw.rect(self.display_surface,UI_BORDER_COLOR_ACTIVE,bg_rect,3) #caso tenha sido alterado a arma ou magia, desenha o retangulo de fundo com borda destacada, indicando que houve mudança
		else:
			pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3) #caso não tenha alterado a arma ou magia desenha o retangulo com borda normal
		return bg_rect

	def weapon_overlay(self,weapon_index,has_switched): #define uma função para fazer a sobreposição das armas
		bg_rect = self.selection_box(10,630,has_switched) #chama a função de caixa de seleção das armas e magias passando a posição do quadro e status da mudança
		weapon_surf = self.weapon_graphics[weapon_index] #cria uma variável com os dados do gráfico da arma
		weapon_rect = weapon_surf.get_rect(center = bg_rect.center) #cria uma variável do retangulo do gráfico da arma

		self.display_surface.blit(weapon_surf,weapon_rect) #desenha o gráfico da arma no retangulo

	def magic_overlay(self,magic_index,has_switched): #define uma função para fazer a sobreposição das magias
		bg_rect = self.selection_box(92,630,has_switched) #chama a função de caixa de seleção das armas e magias passando a posição do quadro e status da mudança
		magic_surf = self.magic_graphics[magic_index] #cria uma variável com os dados do gráfico da magia
		magic_rect = magic_surf.get_rect(center = bg_rect.center) #cria uma variável do retangulo do gráfico da magia

		self.display_surface.blit(magic_surf,magic_rect) #desenha o gráfico da magia no retangulo

	def display(self,player): #define uma função para fazer display dos objetos na tela do jogo
		self.show_bar(player.health,player.stats['health'],self.health_bar_rect,HEALTH_COLOR) #chama a função para mostrar a vida do jogador
		self.show_bar(player.energy,player.stats['energy'],self.energy_bar_rect,ENERGY_COLOR) #chama a função para mostrar a energia do jogador

		self.show_exp(player.exp) #chama a função para mostrar a esperiência do jogador

		self.weapon_overlay(player.weapon_index,not player.can_switch_weapon) #chama a função de para fazer a sobreposição das armas
		self.magic_overlay(player.magic_index,not player.can_switch_magic) #chama a função de para fazer a sobreposição das armas