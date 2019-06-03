from random import randint

import pygame, sys
pygame.init()


def print(*a, **b):
    import builtins, sys
    builtins.print(*a, **b)
    sys.stdout.flush()
    
    
#couleur
NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

#ecran
taille = [700, 500]
ecran = pygame.display.set_mode(taille)

#image
image_perso = pygame.image.load('cessau.png').convert_alpha()
image_perso_tournee = pygame.transform.rotozoom(image_perso, 180, 0.5)
monstre = pygame.image.load('monstre.png').convert_alpha()
monstre_petit = pygame.transform.rotozoom(monstre, 360, 0.09)
#variable
a=100
b=80
r=5
sens=1 
monstre_x= 10
monstre_y= 10



QQQ = 97
SHIFT = 304

clock = pygame.time.Clock()

fini = 0


compteur_monstre = 0

class Monstre:
    pass
bibi = Monstre()
bibi.x = monstre_x
bibi.y = monstre_y

les_monstres=list()  # []
les_monstres.append(bibi)


class Etoile:
    pass

#bibi = Etoile()
#bibi.x = randint(0,700)
#bibi.y = randint(0,500)

#boubou = Etoile()
#boubou.x = randint(0,700)
#boubou.y = randint(0,500)

#truc = Etoile()
#truc.x = randint(0,700)
#truc.y = randint(0,500)

#troc = Etoile()
#troc.x = randint(0,700)
#troc.y = randint(0,500)

les_etoiles = []
#les_etoiles.append(bibi)
#les_etoiles.append(boubou)
#les_etoiles.append(truc)
#les_etoiles.append(troc)

for i in range(40):
    inconnu = Etoile()
    inconnu.x = randint(0,700)
    inconnu.y = randint(0,500)
    les_etoiles.append(inconnu)

print(len(les_etoiles))

# DÉBUT

clock = pygame.time.Clock()
a=600
fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    pressed = pygame.key.get_pressed()
    if pressed[QQQ]:
        b = b - r 
    if b < 20:
        b = 20
    if b > 680:
        b = 680
    if pressed[100]:
        b = b + r
    buttons = pygame.mouse.get_pressed() 
    if b > 450:
        b=450
        
    elif b < 0:
        b=0

    
    compteur_monstre += 1
    if compteur_monstre == 100:
        compteur_monstre = 0
        monstre_y+=10
    
    if monstre_y>450:
        monstre_x+=50
        monstre_y=0
 
    
    # DESSIN
    ecran.fill(NOIR)
    
    #future alien    
    #pygame.draw.rect(ecran, ROUGE, [500,200, 20,40])
    
    #pygame.draw.circle(ecran, BLANC, [bibi.x, bibi.y], 2)
    #pygame.draw.circle(ecran, BLANC, [les_etoiles[0].x, les_etoiles[0].y], 2)
    #pygame.draw.circle(ecran, BLANC, [les_etoiles[1].x, les_etoiles[1].y], 2)
    #pygame.draw.circle(ecran, BLANC, [les_etoiles[2].x, les_etoiles[2].y], 2)
    #pygame.draw.circle(ecran, BLANC, [les_etoiles[3].x, les_etoiles[3].y], 2)
    
    i = 0
    while i < len(les_etoiles):
        pygame.draw.circle(ecran, BLANC, [les_etoiles[i].x, les_etoiles[i].y], 2)
        i = i + 1
    #pygame.draw.circle(ecran, BLANC, [les_etoiles[i].x, les_etoiles[i].y], 2)
    #i = i + 1
    #pygame.draw.circle(ecran, BLANC, [les_etoiles[i].x, les_etoiles[i].y], 2)
    #i = i + 1
    #pygame.draw.circle(ecran, BLANC, [les_etoiles[i].x, les_etoiles[i].y], 2)
    #i = i + 1
    #pygame.draw.circle(ecran, BLANC, [les_etoiles[i].x, les_etoiles[i].y], 2)
    #i = i + 1    
    
    #pygame.draw.circle(ecran, BLANC, [10,500], 2)
    #pygame.draw.circle(ecran, BLANC, [30,650], 2)
    #pygame.draw.circle(ecran, BLANC, [60,250], 2)
    #pygame.draw.circle(ecran, BLANC, [200,200], 2)
    #pygame.draw.circle(ecran, BLANC, [300,10], 2)
    #pygame.draw.circle(ecran, BLANC, [300,200], 2)
    #pygame.draw.circle(ecran, BLANC, [56,279], 2)
    #pygame.draw.circle(ecran, BLANC, [262,305], 2)
    #pygame.draw.circle(ecran, BLANC, [50,200], 2)
    #pygame.draw.circle(ecran, BLANC, [50,200], 2)
    #pygame.draw.circle(ecran, BLANC, [50,200], 2)	
    #pygame.draw.circle(ecran, BLANC, [50,200], 2)
    #pygame.draw.circle(ecran, BLANC, [50,200], 2)
    
    
    # pygame.draw.polygon(ecran, ROUGE, [[0,50], [100,0], [100,100]])
    if sens == -1:
        ecran.blit(image_perso_tournee, [a, b])
    else:
        ecran.blit(image_perso_tournee, [a,b])

        ecran.blit(monstre_petit, [monstre_x, monstre_y])
    pygame.display.flip()
        
    clock.tick(128)
        
pygame.quit()