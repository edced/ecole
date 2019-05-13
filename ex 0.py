#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()



#ecran
taille = [700, 500]
ecran = pygame.display.set_mode(taille)

#image
image_perso = pygame.image.load('cessau.png').convert_alpha()
image_perso_tournee = pygame.transform.rotozoom(image_perso, 90, 0.5)




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
    if a>750:
        sens=-1
    
    
    # DESSIN
    ecran.fill(BLANC)
        
    pygame.draw.rect(ecran, ROUGE, [500,200, 20,40])
    pygame.draw.circle(ecran, BLEU, [50,200], 20)
    pygame.draw.circle(ecran, VERT, [a, b], 10)
    ecran.blit(image_perso_tournee,[350, 450])
    # pygame.draw.polygon(ecran, ROUGE, [[0,50], [100,0], [100,100]])
    if sens == -1:
        pygame.draw.polygon(ecran, ROUGE, [
            [a + 0, 50],
            [a + 100, 0],
            [a + 100, 100]])
    else:
        pygame.draw.polygon(ecran, ROUGE, [
            [a + 100, 50],
            [a + 0, 0],
            [a + 0, 100]])

    pygame.display.flip()
        
    clock.tick(120)
        
pygame.quit()