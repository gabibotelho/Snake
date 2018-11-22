import pygame
from pedaco import Pedaco

class Cobra():

    def __init__(self, cor, largura, altura, x, y):
        super().__init__()
        self.corpo = pygame.sprite.Group()
        cabeca = Pedaco(cor, largura, altura, x, y)
        self.corpo.add(cabeca)
        self.direcao = 'direita'
        self.cor = cor

    def mudar_direcao(self, tecla):
        if tecla[pygame.K_UP]:
            self.direcao = 'cima'
        if tecla[pygame.K_DOWN]:
            self.direcao = 'baixo'
        if tecla[pygame.K_RIGHT]:
            self.direcao = 'direita'
        if tecla[pygame.K_LEFT]:
            self.direcao = 'esquerda'

    def sair(self, tecla):
        if tecla[pygame.K_ESCAPE]:
            pygame.quit()
            exit()

    def mover(self):
        print("mover")
        print(len(self.corpo))
        lista = list(self.corpo)
        xCabeca = lista[len(lista)-1].rect.x
        yCabeca = lista[len(lista)-1].rect.y

        print(xCabeca, yCabeca)
        if self.direcao == "cima":
            if yCabeca < 0:
                yCabeca = 440
            pedaco = Pedaco(self.cor, 15, 15, xCabeca, yCabeca -16)
            self.corpo.add(pedaco)
            self.corpo.remove(lista[0])

        if self.direcao == "baixo":
            if yCabeca > 440:
                yCabeca = -15
            pedaco = Pedaco(self.cor, 15, 15, xCabeca, yCabeca + 16)
            self.corpo.add(pedaco)
            self.corpo.remove(lista[0])

        if self.direcao == "direita":
            if xCabeca > 510:
                xCabeca = -15
            pedaco = Pedaco(self.cor, 15, 15, xCabeca+16, yCabeca)
            self.corpo.add(pedaco)
            self.corpo.remove(lista[0])

        if self.direcao == "esquerda":
            if xCabeca < 0:
                xCabeca = 510
            pedaco = Pedaco(self.cor, 15, 15, xCabeca - 16, yCabeca)
            self.corpo.add(pedaco)
            self.corpo.remove(lista[0])

    def crescer(self):
        lista = list(self.corpo)
        xCabeca = lista[len(lista) - 1].rect.x
        yCabeca = lista[len(lista) - 1].rect.y

        print(xCabeca, yCabeca)
        if self.direcao == "cima":
            pedaco = Pedaco(self.cor, 15, 15, xCabeca, yCabeca - 16)
            self.corpo.add(pedaco)

        if self.direcao == "baixo":
            pedaco = Pedaco(self.cor, 15, 15, xCabeca, yCabeca + 16)
            self.corpo.add(pedaco)

        if self.direcao == "direita":
            pedaco = Pedaco(self.cor, 15, 15, xCabeca + 16, yCabeca)
            self.corpo.add(pedaco)

        if self.direcao == "esquerda":
            pedaco = Pedaco(self.cor, 15, 15, xCabeca - 16, yCabeca)
            self.corpo.add(pedaco)
