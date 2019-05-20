#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()


def print(*a, **b):
    import builtins, sys
    builtins.print(*a, **b)
    sys.stdout.flush()
    

#ecran
taille = [700, 500]
ecran = pygame.display.set_mode(taille)

#image
image_perso = pygame.image.load('cessau.png').convert_alpha()
image_perso_tournee = pygame.transform.rotozoom(image_perso, 90, 0.5)

#touche
while True:
    image_perso_tournee = pygame.transform.rotozoom(image_perso, 90, 0.5)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_d:
                a=a+5
            elif event.key == K_q:
                a=a-5
    pygame.display.update()


#couleur
NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]


#variable
a=100
b=80




# DÉBUT

clock = pygame.time.Clock()
a=600
sens = -1
fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    if sens==1:
        a=a+5
    else:
        a=a-5
      
    
    if a< 0:
        sens=1
    if a>650:
        sens=-1
    
    
    # DESSIN
    ecran.fill(BLANC)
    
    #future alien    
    #pygame.draw.rect(ecran, ROUGE, [500,200, 20,40])
    #pygame.draw.circle(ecran, BLEU, [50,200], 20)
    
    
    
    # pygame.draw.polygon(ecran, ROUGE, [[0,50], [100,0], [100,100]])
    if sens == -1:
        ecran.blit(image_perso_tournee, [a, 400])
    else:
        ecran.blit(image_perso_tournee, [a, 400])

    pygame.display.flip()
        
    clock.tick(64)
        
pygame.quit()