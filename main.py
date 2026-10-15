import pygame
import sys

pygame.init()

# pantalla
WIDTH = 900
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('mario game')
clock = pygame.time.Clock()

# colores
sky = (135, 206, 235)
GREEN = (50, 180, 70)
BROWN = (150, 90, 40)
RED = (220, 40, 40)
BLUE = (40, 80, 220)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 220, 0)

# jugador
player = pygame.Rect(100, 50, 40, 50)
velocity_y = 0
speed = 5
jump_power = -13
gravity = 0.6
on_ground = False

# plataformas
platforms = [
    pygame.Rect(0, 450, 900, 50),
    pygame.Rect(200, 370, 150, 20),
    pygame.Rect(450, 300, 150, 20),
    pygame.Rect(700, 380, 120, 20),
]

# monedas
coins = [
    pygame.Rect(250, 410, 20, 20),
    pygame.Rect(500, 270, 20, 20),
    pygame.Rect(740, 340, 20, 20),
]

score = 0
font = pygame.font.Font(None, 36)

running = True

while running:
    # Evento
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP] and on_ground:
        velocity_y = jump_power
        on_ground = False

    # gravedad
    velocity_y += gravity
    player.y += velocity_y

    on_ground = False
    for ground in platforms:
        if player.colliderect(ground):
            if velocity_y >= 0:
                player.bottom = ground.top
                velocity_y = 0
                on_ground = True

    # límite de pantalla
    if player.x < 0:
        player.x = 0
    if player.x + player.width > WIDTH:
        player.x = WIDTH - player.width
    if player.y > HEIGHT:
        player.y = HEIGHT - player.height
        velocity_y = 0
        on_ground = True

    # monedas
    for coin in coins[:]:
        if player.colliderect(coin):
            coins.remove(coin)
            score += 10

    # dibujar
    screen.fill(sky)

    for ground in platforms:
        pygame.draw.rect(screen, GREEN, ground)

    for coin in coins:
        pygame.draw.circle(screen, YELLOW, (coin.centerx, coin.centery), 10)

    pygame.draw.rect(screen, BLUE, player)

    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
