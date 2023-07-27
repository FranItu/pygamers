# Creditos
# Pygamers
# Francis, Sebas, Alex, Alejo 
# Testing 1
# 
# 
# 
# 

"""
LIBRERIAS
"""
import os
import pygame
import random
import numpy as np
#os.chdir('./Project2')


"""
SETTINGS
"""
#Ventana
WID, HEI = 640, 576
WIN = pygame.display.set_mode((WID, HEI))
pygame.display.set_caption("Project 2")
FPS = 24
seed = (random.randint(0,5000),random.randint(0,5000))

#Colores
BLANCO = (255,255,255)
NEGRO = (0,0,0)
WIN.fill(NEGRO)

"""
ASSETS
"""
#PLAYERS
##Dimensions
PW, PH = 30, 40

##Icons
P1_IMAGE = pygame.image.load(
    os.path.join('Assets', 'BRENDAN.png')
    )
P1 = pygame.transform.scale(P1_IMAGE, (PW, PH))
P2_IMAGE = pygame.image.load(
    os.path.join('Assets', 'MEW.png')
    )
P2 = pygame.transform.scale(P2_IMAGE, (PW, PH))
P3_IMAGE = pygame.image.load(
    os.path.join('Assets', 'MAY.png')
    )
P3 = pygame.transform.scale(P3_IMAGE, (PW, PH))
#pygame.transform.rotate(surface, angle)

#Background
BG_IMAGE = pygame.image.load(
    os.path.join('Assets', 'BG_Sootopolis_Gym.png')
    )
BG = pygame.transform.scale(BG_IMAGE, (WID, HEI))

"""
GAME
"""
#Window Update
def draw_start():
    WIN.fill(NEGRO)
    font1 = pygame.font.SysFont('castellar', 48)
    font2 = pygame.font.SysFont('castellar', 32)
    title = font1.render('Project 2', True, BLANCO)
    start_button = font2.render('Start', True, (0, 128, 255))
    quit_button = font2.render('Quit', True, (255, 0, 0))
    WIN.blit(title, (WID/2 - title.get_width()/2, HEI/4 - title.get_height()/2))
    WIN.blit(start_button, (WID/2 - start_button.get_width()/2, 3*HEI/5 - start_button.get_height()/2))
    WIN.blit(quit_button, (WID/2 - quit_button.get_width()/2, 4*HEI/5 - quit_button.get_height()/2))
    pygame.display.update()

def draw_window(c1, c2, c3):
    WIN.fill((c1,c2,c3))
    WIN.blit(BG, (0,0))
    WIN.blit(P1, (150,2*c1))
    WIN.blit(P2, (325,2*c2))
    WIN.blit(P3, (500,2*c3))
    pygame.display.update()

def draw_window2(p1, p2, p3):
    WIN.fill(NEGRO)
    WIN.blit(BG, (0,0))
    WIN.blit(P1, (p1.x, p1.y))
    WIN.blit(P2, (p2.x, p2.y))
    WIN.blit(P3, (p3.x, p3.y))
    pygame.display.update()

#Main Game
def game():
    #Variable de Juego
    game_state = "Inicio"

    #Atributos Jugadores
    redp = pygame.Rect(150, 100, PW, PH)
    yellowp = pygame.Rect(325, 100, PW, PH)
    bluep = pygame.Rect(500, 100, PW, PH)

    #Reloj
    clock = pygame.time.Clock()

    #Inicio
    while game_state == "Inicio":
        draw_start()
        pressedkey = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("GAME OVER")
                game_state = "Gameover"

        if pressedkey[pygame.K_ESCAPE]:
            print("GAME OVER")
            game_state = "Gameover"
        
        if pressedkey[pygame.K_RETURN] or pressedkey[pygame.K_SPACE]:
            print("Starting game...")
            game_state = "Playing"

    #Juego
    while game_state == "Playing":
        clock.tick(FPS)
        desp = 2 #desplazamiento

        #Events
        pressedkey = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("GAME OVER")
                game_state = "Gameover"

        # Progress Conditions
        ## Player 1
        if pressedkey[pygame.K_s]:
            redp.y += desp
        if pressedkey[pygame.K_w]:
            redp.y -= desp
        if pressedkey[pygame.K_d]:
            redp.x += desp
        if pressedkey[pygame.K_a]:
            redp.x -= desp

        ## Player 3
        if pressedkey[pygame.K_DOWN]:
            bluep.y += desp
        if pressedkey[pygame.K_UP]:
            bluep.y -= desp
        if pressedkey[pygame.K_RIGHT]:
            bluep.x += desp
        if pressedkey[pygame.K_LEFT]:
            bluep.x -= desp

        ## Player 2 (NPC)
        # dist j1 j2
        d12 = np.sqrt((redp.x - yellowp.x)**2 + (redp.y - yellowp.y)**2)
        # dist j3 j2
        d32 = np.sqrt((bluep.x - yellowp.x)**2 + (bluep.y - yellowp.y)**2)
        
        if d12 < d32:
            yellowp.x += -np.sign(redp.x - yellowp.x)*desp/2
            yellowp.y += -np.sign(redp.y - yellowp.y)*desp/2
        elif d32 < d12:
            yellowp.x += -np.sign(bluep.x - yellowp.x)*desp/2
            yellowp.y += -np.sign(bluep.y - yellowp.y)*desp/2
        else:
            yellowp.y += random.randint(-desp, desp)
            yellowp.x += random.randint(-desp, desp)
        
        #Teleport
        rand1 = random.randint(0,5000)
        if (np.absolute(rand1 - seed[0]) % 400) == 0:
            yellowp.x = rand1 % WID
        if (np.absolute(rand1 - seed[1]) % 400) == 0:
            yellowp.y = rand1 % HEI

        # Winning Conditions
        if ((redp.x >= yellowp.x-3) and (redp.x <= yellowp.x+3) and (redp.y >= yellowp.y-3) and (redp.y <= yellowp.y+3)):
            print("Winner: Player 1")
            game_state = "VictoryP1"
            continue

        if ((bluep.x >= yellowp.x-3) and (bluep.x <= yellowp.x+3) and (bluep.y >= yellowp.y-3) and (bluep.y <= yellowp.y+3)):
            print("Winner: Player 2")
            game_state = "VictoryP2"
            continue

        #Losing condition
        if ((yellowp.x < 0) or (yellowp.x > WID) or (yellowp.y < 0) or (yellowp.y > HEI)):
            print("Game Over! Mew scaped.")
            game_state = "Defeat"
            continue

        #if (redp.y >= 255 or yellowp.y >= 255 or bluep.y >= 255):
        #    playerdicty = {"Player 1": redp.y, "Player 2": yellowp.y, "Player 3": bluep.y}
        #    print("Winner: ", max(playerdicty, key=playerdicty.get))
        #    run = False
        #    continue
        
        #Update
        draw_window2(redp, yellowp, bluep)

    pygame.quit()

# Proper Running
if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    game()


##### THANK YOU FOR PLAYING
# Hola
#
