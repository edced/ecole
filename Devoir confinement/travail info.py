from random import randint

import pygame, sys
pygame.init()


def print(*a, **b):
    import builtins, sys
    builtins.print(*a, **b)
    sys.stdout.flush()



fini = 1
ENTER = 13

if fini == 1:
    print("1. a bit is the smallest unit of data on a pc. Source: https://whatis.techtarget.com/definition/bit-binary-digit")
    fini = 0
if fini == 0:
    print("press enter to continue")
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == ENTER:  # pygame.K_RETURN
                fini = 1

if fini == 1:
    print("2. In most computer systems, a byte is a unit of data that is eight binary digits long. Source: https://searchstorage.techtarget.com/definition/byte")
    print("press enter to continue")

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == ENTER:  # pygame.K_RETURN
                fini = 0
                

while fini == 1:
    print("3. 0, 1, 10, 11, 100, 101, 111, 1000, 1001, 1010, 1011, 1100 1101 1110 1111 10000 10001 10010 10100 10101 10111 11000 11001 11010 11011 11100 11101 11110 11111 100000 100001 100010 100011 100100 100101 100110 100111 101000. Source: https://www.convertbinary.com/numbers/    ps: J'ai pas vraiment compris comment faire")
    print("press enter to continue")
    fini = 0
while fini == 0:    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == ENTER:  # pygame.K_RETURN
                fini = 1  

                
while fini == 1:
    print("4. 1 2 3 4 5 6 7 8 9 A B C D E F 10 11 12 13 14 115 16 17 18 19 1A 1B 1C 1D 1E 1F 20 21 22 23 24 25 26 27 28 29 2A 2B... source: https://www.rapidtables.com/convert/number/decimal-to-hex.html?x=42")
    print("press enter to continue")
    fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == ENTER:  # pygame.K_RETURN
                fini = 1


while fini == 1:
    print("5. 6. 7. Github ")
    print("press enter to continue")
    fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == ENTER:  # pygame.K_RETURN
                fini = 1
                
            



        
    

