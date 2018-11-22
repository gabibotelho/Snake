import pygame, random
from cobra import Cobra
from frutinha import Frutinha


# cores
VERDE = (0, 255, 0)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

pygame.init()
pygame.font.init()
fonte = pygame.font.SysFont('Calibri', 28)
pontos = 0
LARGURA = 510
ALTURA = 440

tela = pygame.display.set_mode([LARGURA, ALTURA])

GAMEOVER = "Game over"
fontefim = 'freesansbold.ttf'
GAMEOVERCOLOR = VERMELHO
CENTER = (255, 220)

frutinhas = pygame.sprite.Group()
todosObjetos = pygame.sprite.Group()

x = random.randrange(LARGURA)
y = random.randrange(ALTURA)
frutinha = Frutinha(VERMELHO, 9, 9, x, y)
frutinhas.add(frutinha)

x = random.randrange(LARGURA)
y = random.randrange(ALTURA)
cobra = Cobra(VERDE, 15, 15, x, y)
todosObjetos.add(cobra.corpo)
todosObjetos.add(frutinhas)
terminou = False
clock = pygame.time.Clock()
lastmove = pygame.time.get_ticks()

while True:
    clock.tick(30)
    filaEventos = pygame.event.get()
    for evento in filaEventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.KEYDOWN:
            tecla = pygame.key.get_pressed()
            cobra.mudar_direcao(tecla)

        if evento.type == pygame.KEYDOWN:
            tecla = pygame.key.get_pressed()
            cobra.sair(tecla)

    if pygame.time.get_ticks()-lastmove >= 200:
        lastmove = pygame.time.get_ticks()
        todosObjetos.remove(cobra.corpo)
        cobra.mover()
        todosObjetos.add(cobra.corpo)
        lista = []
        lista = pygame.sprite.groupcollide(cobra.corpo, frutinhas, False, True)
        pontos += len(lista)

        if len(lista) > 0:
            cobra.crescer()
            x = random.randrange(LARGURA)
            y = random.randrange(ALTURA)
            frutinha = Frutinha(VERMELHO, 9, 9, x, y)
            frutinhas.add(frutinha)
            todosObjetos.add(frutinhas)
        for pedaco in cobra.corpo:
            lista = pygame.sprite.spritecollide(pedaco, cobra.corpo, False)
            print(len(lista))
            if len(lista) > 1:
                print("game over")
                tela.fill(PRETO)
                font = pygame.font.Font(fontefim, 30)
                text_surface = font.render(GAMEOVER, True, GAMEOVERCOLOR)
                text_rect = text_surface.get_rect()
                text_rect.center = CENTER
                tela.blit(text_surface, text_rect)
                pygame.display.update()
                pygame.time.wait(5000)
                pygame.quit()
                exit()

    texto = fonte.render("Pontos: " + str(pontos), True, (VERDE))

    tela.fill(PRETO)
    tela.blit(texto, (0, 0))
    todosObjetos.draw(tela)
    pygame.display.update()
