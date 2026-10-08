import pygame 
import sys
pygame.init()

# comfigurando
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Game")
BLACK=(0,0,0)

def game_loop():
    print("Game started!") # marcador de posicion por hora

def start_game():
    canvas.fill(BLACK)
    start_img=pygame.image.load('start.png')
    start_img_rect=start_img.git_rect()
    start_img_rect.center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2)
    canvas.blit(start_img,start_img_rect)

    while True:
        for event in pygame.event.git():
            if event.type==pygame.QUIT:
                pygame.exit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:

                    pygame.quit()
                    sys.exit()
                game_loop()
        