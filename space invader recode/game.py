from random import randint

import pygame, sys
pygame.init()


def print(*a, **b):
    import builtins, sys
    builtins.print(*a, **b)
    sys.stdout.flush()

# ###VAR START
#COLOR
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]

#KEYS
ENTER = 13
M = 109
SPACE = 32


#INGAME VAR
SOUND=1

# ###VAR END

# ###SCREEN START
size = [700, 500]
screen = pygame.display.set_mode(size)
# ###SCREEN END

# ###ELEMENTS START

# IMAGES START

#RED GHOST
BIG_R_GHOST = pygame.image.load('Ghost_R.png').convert_alpha()
R_GHOST = pygame.transform.rotozoom(BIG_R_GHOST, 0, 0.07)

#GREEN GHOST
BIG_G_GHOST = pygame.image.load('Ghost_G.png').convert_alpha()
G_GHOST = pygame.transform.rotozoom(BIG_G_GHOST, 0, 0.09)

#YELLOW GHOST
BIG_Y_GHOST = pygame.image.load('Ghost_Y.png').convert_alpha()
Y_GHOST = pygame.transform.rotozoom(BIG_Y_GHOST, 0, 0.09)

#SPACESHIP
BIG_SS = pygame.image.load('SpaceShip.png').convert_alpha()
SS = pygame.transform.rotozoom(BIG_SS, 90, 0.5)
#FONT
FONT = pygame.font.SysFont('Calibri', 25)
BIG_FONT = pygame.font.SysFont('Calibri', 50)


#SOUND

SHOOT_SOUND = pygame.mixer.Sound("PEW.wav")


#function

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










# ###INTRO

#vars
text_blink = 0
clock = pygame.time.Clock()
end = 0
l,h = G_GHOST.get_size()

#game intro
while end == 0:
    
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = 0
        elif event.type == pygame.KEYDOWN:
                end = 1
                print("DEBUG: Key number", event.key, "was pressed ")

        elif event.type == pygame.MOUSEBUTTONDOWN:
                end = 1
                print("DEBUG: mouse pressed")
    
    #screen
    screen.fill(BLACK)
    #ghosts
    screen.blit(G_GHOST, [100, 350])     
    screen.blit(Y_GHOST, [100, 250])
    screen.blit(R_GHOST, [100, 150])
    #text
    intro_text = BIG_FONT.render("Space Invader (r)", True, WHITE) 
    texte_start = BIG_FONT.render("Press any key to start", True, RED)
    blit_center(screen, intro_text, [350, 50])
    


    text_center(screen, "This is a red monster, he dies in one hit", FONT, WHITE, [355, 150 + h/2])
    text_center(screen, "This is a yellow monster, he dies in two hits", FONT, WHITE, [378, 250 + h/2])
    text_center(screen, "This is a green monster, he dies in three hits", FONT, WHITE, [380, 350 + h/2])
    

    text_blink += 1
    if text_blink < 50:
        blit_center(screen, texte_start, [350, 450])
    elif text_blink == 100:
        text_blink = 0

    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
