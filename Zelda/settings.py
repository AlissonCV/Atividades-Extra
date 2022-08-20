#!/usr/bin/python3

#Configurações do Jogo (Variáveis da biblioteca main - principal)
WIDTH	 = 1280 #Largura  da Tela
HEIGHT	 = 720 #Altura da Tela
FPS	 = 128 #Numero de Telas por Segundo
TILESIZE = 64 #Tamanho do Ladrilho (Malha)

HITBOX_OFFSET = {
	'player': -26,
	'object': -40,
	'grass': -10,
	'invisible': 0}

# ui - variáveis da Interface de Usuário
BAR_HEIGHT = 20 #largura da barra de status
HEALTH_BAR_WIDTH = 200 #altura da barra de status de vida
ENERGY_BAR_WIDTH = 140 #altura da barra de status de energia
ITEM_BOX_SIZE = 80 #tamanho da caixa de itens (armas/energias)
UI_FONT = 'graphics/font/joystix.ttf' #fonte gráfica a ser usada na interface de usuário
UI_FONT_SIZE = 18 #define o tamanho da fonte da Interface Grafica

# cores gerais do jogo
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111' #define uma cor padrão para a borda
TEXT_COLOR = '#EEEEEE'

# cores da Interface de Usuário
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold' #cor de destaque da borda ativa das seleções das armas e magias

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# Define as armas que podem ser usadas no jogo
weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15,'graphic':'graphics/weapons/sword/full.png'},
	'lance': {'cooldown': 400, 'damage': 30,'graphic':'graphics/weapons/lance/full.png'},
	'axe': {'cooldown': 300, 'damage': 20, 'graphic':'graphics/weapons/axe/full.png'},
	'rapier':{'cooldown': 50, 'damage': 8, 'graphic':'graphics/weapons/rapier/full.png'},
	'sai':{'cooldown': 80, 'damage': 10, 'graphic':'graphics/weapons/sai/full.png'}}

# Variáveis para as Magias
magic_data = {
	'flame': {'strength': 5,'cost': 20,'graphic':'graphics/particles/flame/fire.png'}, #parâmetros da magia fogo
	'heal' : {'strength': 20,'cost': 10,'graphic':'graphics/particles/heal/heal.png'}} #parâmetros da magia cura

# Variáveis para inimigos
#health: vida do inimigo
#exp: esperiência do inimigo
#damage: poder de destruição do inimigo
#attack_tipe: tipos de ataques (slash=golpe; claw=garra; thunder=trovão; leaf_attack=ataque leve)
#resistance: resistência do inimigo, coordenadas em que o inimigo afasta após ser atacado
#attack_radius: raio em torno do inimigo em que ele irá atacar o jogador
#notice_radius: raio em que o inimigo irá notar a presença do jogador e irá mover até ele
monster_data = {
	'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':'audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}
