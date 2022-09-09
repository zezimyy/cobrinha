import pygame
from sys import exit
from pygame.locals import *
import random

pygame.init()

#tela
largura=400
altura=400
tela = pygame.display.set_mode((largura, altura))

#player
x_player = largura/2
y_player = altura/2

#moeda
x_moeda = random.randint(40, 360)
y_moeda = random.randint(40, 360)

#pontos
pontos = 0
fonte = pygame.font.SysFont("arial", 30, False, False)

#relogio
relogio = pygame.time.Clock()

lista_cobra = []

def aumenta_cobra(lista_cobra):
  for XeY in lista_cobra:
    pygame.draw.rect(tela, (0,0,255), (XeY[0], XeY[1], 20, 20))
    
while True:
    relogio.tick(60)
    tela.fill((255,255,255))

    mensagem = f"pontos: {pontos}"
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))
  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    player = pygame.draw.rect(tela, (0,0,255), (x_player, y_player, 20, 20))
    moeda = pygame.draw.circle(tela, (255,0,0), (x_moeda, y_moeda), 5)

    if pygame.key.get_pressed()[K_a]:
        x_player = x_player - 3
      
    if pygame.key.get_pressed()[K_d]:
        x_player = x_player + 3
      
    if pygame.key.get_pressed()[K_w]:
        y_player = y_player - 3
      
    if pygame.key.get_pressed()[K_s]:
        y_player = y_player + 3

    if player.colliderect(moeda):
        x_moeda = random.randint(40,360)
        y_moeda = random.randint(40,360)
        pontos = pontos + 1

    

    #criar corpo da cobra
    lista_cabeca = []
    lista_cabeca.append(x_player)
    lista_cabeca.append(y_player)
    
    lista_cobra.append(lista_cabeca)

    aumenta_cobra(lista_cobra)
  
    tela.blit(texto_formatado, (250, 20))
    pygame.display.update()