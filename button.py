class Button():	#Criação da classe Button para chamadas externas
  def __init__(self, image, pos, text_input, font, base_color, hovering_color):	#Função com entrada de valores de carregamento de imagem, posição, texto, tipo de fonte, cor inicial e cor de mudança de estado
    self.image = image	#Atribuição na variável "self.image" da imagem que deve ser carregada
    self.pos = pos	#Atribuição na variável "self.pos" da posição onde o botão sera desenhado
    self.font = font	#Atribuição na variável "self.font" do tipo e tamanho da fonte que será utilizada
    self.base_color, self.hovering_color = base_color, hovering_color	#Atribuição nas variáveis "self.base_color" e "self.hovering_color" da cor inicial e a cor de mudança de estado
    self.text_input = text_input	#Atribuição na variável "self.text_input" do texto que sera colocado no botão
    self.text = self.font.render(self.text_input, True, self.base_color)	#Atribuição na variável "self.text" das definiçoes do texto e da cor que será impresso
    if self.image is None:	#Verificação se não existe carregamento de imagem 
      self.image = self.text	#Atribuição do texto como uma imagem para dimencionamento do tamanho da caixa
    self.rect = self.image.get_rect(center=self.pos)	#Atribuição na variável "self.rect" de uma caixa centralizada na posição definida
    self.text_rect = self.text.get_rect(center=pos)	#Atribuição na variável "self.text_rect" da posição onde o texto será colocado

  def update(self, screen):	#Função de atualização da imagem da caixa na tela
    if self.image is not None:	#Verificação se não existe carregamento de imagem 
      screen.blit(self.image, self.rect)	#Desenho do texto na tela
    screen.blit(self.text, self.text_rect)	#Desenho do texto dentro da caixa na tela

  def checkForInput(self, position):	#Função de verificação da posição do mouse quando foi clicado
    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom): #Vericicação se o mouse esta na posição detro da caixa criada
      return True	#Retorno de confirmação para mudança de tela
    return False	#Retorno de negação para mudança de tela

  def changeColor(self, position):	#Função de mudança de cor de acordo com a posição do mouse
    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):	#Vericicação se o mouse esta na posição detro da caixa criada
      self.text = self.font.render(self.text_input, True, self.hovering_color)	#Mudança da cor da variável
    else:	#Retorno para quando a verifição indicar que o mouse não esta dentro da caixa criada
      self.text = self.font.render(self.text_input, True, self.base_color)	#Mudança da cor da variável
