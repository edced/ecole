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
ENTER = 13
M = 109
#ecran
taille = [700, 500]
ecran = pygame.display.set_mode(taille)

#image
image_perso = pygame.image.load('cessau.png').convert_alpha()
image_perso_tournee = pygame.transform.rotozoom(image_perso, 90, 0.5)
monstre = pygame.image.load('monstre.png').convert_alpha()
monstre_petit = pygame.transform.rotozoom(monstre, 360, 0.09)
monstre_rouge = pygame.image.load('monstre_rouge.png').convert_alpha()
monstre_petit_rouge = pygame.transform.rotozoom(monstre_rouge, 360, 0.07)
monstre_vert = pygame.image.load('monstre_vert.png').convert_alpha()
monstre_petit_vert = pygame.transform.rotozoom(monstre_vert, 360, 0.09)
font = pygame.font.SysFont('Calibri', 25)
font_grand = pygame.font.SysFont('Calibri', 50)

tir_son = pygame.mixer.Sound("PEW.wav")
son = 1

# fonction
def blit_center(surface, image, pos, centre_y=True):
    x = pos[0]
    y = pos[1]
    l = image.get_width()
    h = image.get_height()
    if centre_y == True:
        surface.blit(image, [x-l/2, y-h/2])
    else:
        surface.blit(image, [x-l/2, y])      

def text_center(surface, texte, font, couleur, pos, centre_y=True):
    image = font.render(texte, True, couleur)
    blit_center(surface, image, pos, centre_y)


# ecran d'intro
text_blink = 0
clock = pygame.time.Clock()
fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 0
            perdu = 1
            gagne = 0
            
        
        elif event.type == pygame.KEYDOWN:
            
            if event.key == ENTER:  # pygame.K_RETURN
                fini=1
            if event.key == M:
                if son == 0:
                    son = 1
                elif son == 1:
                    son = 0
            print("DEBUG:son", son)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            fini = 1  
    
    ecran.fill(NOIR)
    
    ecran.blit(monstre_petit_vert, [100, 350])     
    ecran.blit(monstre_petit, [100, 250])
    ecran.blit(monstre_petit_rouge, [100, 150]) 
    texte_intro = font_grand.render("Space Invader (r)", True, BLANC)    
    blit_center(ecran, texte_intro, [350, 50])
    
    l,h = monstre_petit_vert.get_size()
    text_center(ecran, "Ceci est un monstre ROUGE, apres 1 tir, il meurt", font, BLANC, [400, 150 + h/2])
    text_center(ecran, "Ceci est un monstre ORANGE, apres 2 tirs, il meurt", font, BLANC, [400, 250 + h/2])
    text_center(ecran, "Ceci est un monstre VERT, apres 3 tirs, il meurt", font, BLANC, [400, 350 + h/2])
    text_center(ecran, "Y a-t-il du son (appuie sur M):", font, BLANC, [500, 480])
    if son == 0:
        text_center(ecran, "NON", font, ROUGE, [675, 480])
    elif son == 1:
        text_center(ecran, "OUI", font, VERT, [675, 480])
    texte_start = font_grand.render("Click pour commencer", True, ROUGE)
    
    
    
    text_blink += 1
    if text_blink < 30:
        blit_center(ecran, texte_start, [350, 450])
    elif text_blink == 60:
        text_blink = 0
    
    
    
        
                   
    pygame.display.flip()
    
    clock.tick(60)

OBJECTIF = 2500

#variable
a=350
b=450
r=5
score = 0
class Missile:
    pass
missile = Missile()
missile.x = a  # position du missile
missile.y = b
missile.present = 0
sens=1 
monstre_x= 10
monstre_y= 10
liste_missiles = []
temps_attente = 1
QQQ = 97
SHIFT = 304
SPACE= 32
M=109
clock = pygame.time.Clock()


fini = 0


compteur_monstre = 1
compteur_apparition = 1
niveau = 0
class Monstre:
    pass
bibi = Monstre()
bibi.x = monstre_x
bibi.y = monstre_y
bibi.vie = 2
bobo = Monstre()
bobo.x = monstre_x
bobo.y = monstre_y+50
bobo.vie = 1

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

for i in range(100):
    inconnu = Etoile()
    inconnu.x = randint(0,700)
    inconnu.y = randint(0,500)
    les_etoiles.append(inconnu)

print("DEBUG Star #", len(les_etoiles))

#DÉBUT
clock = pygame.time.Clock()
fini = 0
perdu = 1
while fini == 0:
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
            perdu = 0
            gagne = 0
            
        
        elif event.type == pygame.KEYDOWN:
            print("DEBUG : keypress", event.key)
            if event.key == SPACE:
                if son == 1:
                    tir_son.play()
                
                nouveau_missile = Missile()
                nouveau_missile.x = a
                nouveau_missile.y = b
                liste_missiles.append(nouveau_missile)
                print("DEBUG : New Missile")
            
    
    niveau += 10
    
    # TICK
    pressed = pygame.key.get_pressed()
    if pressed[QQQ]:
        a = a - r 
    if a < 20:
        a = 20
    if a > 680:	
        a = 680
    if pressed[100]:
        a = a + r
    buttons = pygame.mouse.get_pressed() 
    if a > 450:
        a=350
        
    elif a < 0:
        a=0
    
    corbeille = []
    for missile in liste_missiles: #pour chacun des missilie dans la liste missile:
        missile.y -= 10
        
        if missile.y < 0:
            corbeille.append(missile) # supprimer missile
            print("DEBUG: missile destroyed")
            
    for x in corbeille:
        liste_missiles.remove(x)
    
    compteur_apparition += 1
    
    if niveau < 3*5000:
        compteur_apparition_max = 100
    elif niveau > 3*5000:
        compteur_apparition_max = 50
    elif niveau > 6*5000:
        compteur_apparition_max = 25
    else:
        compteur_apparition_max = 25
    
    if compteur_apparition >= compteur_apparition_max:
        m = Monstre()
        m.x = 10
        m.y = 0
        m.vie = randint(1, 3)
        les_monstres.append(m)
        compteur_apparition = 0
    
    
    compteur_monstre += 1
    if compteur_monstre == 25:
        compteur_monstre = 0
        
        for m in les_monstres:
            if niveau < 3*5000:
                m.y += 10
            elif niveau > 3*5000:
                m.y += 20
            elif niveau > 6*5000:
                m.y += 30
            else:
                m.y += 30

        
    for m in les_monstres:
        if m.x>100:
            m.y+=50
            m.x=0
        if m.y > 350:
            fini=1
    
    corbeille = []
    corbeille_missile = []
    for m in les_monstres:
        for missile in liste_missiles:
            x = m.x
            y = m.y
            L = monstre_petit_rouge.get_width()
            H = monstre_petit_rouge.get_height()
            bx = missile.x
            by = missile.y
            bL, bH = 30, 10
            
            # question: (inversion logique)
            # if a < 5:
            #    ...
            # else:
            #    print(coco)
            # dans quel cas sera affiché coco ? if not(a < 5) si a n'est pas < 5
            # comment rephraser ça dans utiliser le terme "pas" ?
            # if a >= 5
            
            # question: 
            # if a < 5 or b < 2:
            #    ...
            # else
            #     print(coco)
            # dans quel cas sera affiché coco ?
            # if not(a < 5 or b < 2):
            # if a >= 5 and b >= 2
            
            
            
            #fonction
            #if collision(m.x, m.y, monstre_petit_rouge.get_width(), monstre_petit_rouge.get_height(),
            #             missile.x, missile.y, 30, 10):
            if bx > x + L or bx + bL < x or by > y + H or by + bH < y:
                ...
            else:
                print("DEBUG : hit monster with ", m.vie, "live(s)")
                if m.vie == 1:
                    print("DEBUG : Dead")                    
                    corbeille.append(m)
                    corbeille_missile.append(missile)
                else:
                    m.vie -= 1
                    print("DEBUG New life =", m.vie)
                    score += 10
                    corbeille_missile.append(missile)
                
    
    for m in corbeille:
        if m in les_monstres:
            les_monstres.remove(m)
            score += 10
        if score >= OBJECTIF:
            gagne=1
            fini=1
            perdu = 0
    for m in corbeille_missile:
        if m in liste_missiles:
            liste_missiles.remove(m)
        
    # DESSIN
    ecran.fill(NOIR)
    for missile in liste_missiles:
        pygame.draw.rect(ecran, BLANC, [missile.x, missile.y, 10, 30]) 
    
    pygame.draw.rect(ecran, ROUGE, [545, 0, 1, 350])
    #future alien    
    #pygame.draw.rect(ecran, ROUGE, [500,200, 20,40])
    
    #pygame.draw.circle(ecran, BLANC, [bibi.x, bibi.y], 2)
    #pygame.draw.circle(ecran, BLANC, [les_etoiles[0].x, les_etoiles[0].y], 2)
    #pygame.draw.circle(ecran, BLANC, [les_etoiles[1].x, les_etoiles[1].y], 2)
    #pygame.draw.circle(ecran, BLANC, [les_etoiles[2].x, les_etoiles[2].y], 2)
    #pygame.draw.circle(ecran, BLANC, [les_etoiles[3].x, les_etoiles[3].y], 2)
    
    i = 0
    while i < len(les_etoiles):  # 4
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
    
    if niveau < 3*5000:
        texte = ("niveau 1")
    elif niveau > 3*5000:
        texte = ("niveau 2")
    elif niveau > 6*5000:
        texte = ("niveau 3")
    else:
        texte = ("dernier niveau") 
    image_niveau = font.render(texte, True, BLANC)
    ecran.blit(image_niveau, [0, 0])
    
    
    image_score = font.render("Score: " + str(score), True, BLANC)
    ecran.blit(image_score, [700-125, 0])
    
    # pygame.draw.polygon(ecran, ROUGE, [[0,50], [100,0], [100,100]])
    if sens != 1:
        blit_center(image_perso_tournee, [a, b], True)
    else:  
        ecran.blit(image_perso_tournee, [a, b])

    for m in les_monstres:
        if m.vie == 3:
            ecran.blit(monstre_petit_vert, [m.x, m.y])
        if m.vie == 2:
            ecran.blit(monstre_petit, [m.x, m.y])
        
        if m.vie == 1:
            ecran.blit(monstre_petit_rouge, [m.x, m.y])
            
    
    
    pygame.display.flip()
    
    clock.tick(60)

#endgame
if perdu == 1:
    fini = 0
    gagne = 0
    while fini == 0:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fini = 1        
        
        temps_attente += 1
        
        if temps_attente > 500000:
            fini = 1
        
        ecran.fill(NOIR)
        
        texte_perdu = ("Tu as perdu")
        image_perdu = font.render(texte_perdu, True, BLANC)
        ecran.blit(image_perdu, [300, 250])
               
        pygame.display.flip()
                
        clock.tick(60)

if gagne == 1:
    fini = 0
    while fini == 0:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fini = 1
        
        temps_attente += 1
        if temps_attente > 500:
            fini = 1
        
        ecran.fill(NOIR)
        
        texte_gagne = ("Tu as gagné")
        image_gagne = font.render(texte_gagne, True, BLANC)
        ecran.blit(image_gagne, [300, 250])
               
        pygame.display.flip()
                
        clock.tick(60)    

pygame.quit()