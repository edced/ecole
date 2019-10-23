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
monstre_rouge = pygame.image.load('monstre_rouge.png').convert_alpha()
monstre_petit_rouge = pygame.transform.rotozoom(monstre_rouge, 360, 0.07)
#variable
a=600
b=80
r=5

class Missile:
    pass
missile = Missile()
missile.x = a  # position du missile
missile.y = b
missile.present = 0
sens=1 
monstre_x= 10
monstre_y= 10



QQQ = 97
SHIFT = 304
SPACE= 32
clock = pygame.time.Clock()

fini = 0


compteur_monstre = 1
compteur_apparition = 1

class Monstre:
    pass
bibi = Monstre()
bibi.x = monstre_x
bibi.y = monstre_y
bobo = Monstre()
bobo.x = monstre_x
bobo.y = monstre_y+50

les_monstres=list()  # []
les_monstres.append(bibi)
les_monstres.append(bobo)

    

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

#DÉBUT
clock = pygame.time.Clock()
fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        elif event.type == pygame.KEYDOWN:
            print("coucou", event.key)
            if event.key == SPACE:
                missile.present = 1
                missile.x = a
                missile.y = b
            
    
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
    
    if missile.present == 1:
        missile.x -= 10
        
    if missile.x < 0:
        missile.present = 0
    
    compteur_apparition += 1
    if compteur_apparition == 100:
        m = Monstre()
        m.x = 10
        m.y = 0
        les_monstres.append(m)
        compteur_apparition=0
    
    
    compteur_monstre += 1
    if compteur_monstre == 25:
        compteur_monstre = 0
        
        for m in les_monstres:
            m.y+=10

        
    for m in les_monstres:
        if m.y>450:
            m.x+=50
            m.y=0
    
    corbeille = []
    for m in les_monstres:
        if missile.present == 1:
            x = m.x
            y = m.y
            L,H = monstre_petit_rouge.get_width(), monstre_petit_rouge.get_height()
            bx = missile.x
            by = missile.y
            bL, bH = 30, 10
            if bx > x + L or bx + bL < x or by > y + H or by + bH < y:
                ...
            else:
                corbeille.append(m)
                missile.present = 0
    
    for m in corbeille:
        les_monstres.remove(m)
        
    # DESSIN
    ecran.fill(NOIR)
    if missile.present == 1:
        pygame.draw.rect(ecran, BLANC, [missile.x, missile.y, 30, 10]) 
    
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
        ecran.blit(image_perso_tournee, [a, b])

    for m in les_monstres:
        if m == bibi:
            ecran.blit(monstre_petit, [m.x, m.y])
        else:
            ecran.blit(monstre_petit_rouge, [m.x, m.y])
            
    
    
    pygame.display.flip()
    clock.tick(60)
        
pygame.quit()