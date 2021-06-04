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

