# Creating an empty screen that can be closed
import pygame
# initializing pygame
pygame.init()

# creating a screen
screen = pygame.display.set_mode((240, 180))

# loading and setting logo and title
#logo = pygame.image.load("logo32x32.png")
#pygame.display.set_icon(logo)
pygame.display.set_caption("First pygame")

x = 50
y = 50
h = 20
w = 20
v = 5

running = True
while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        # adding option to quit anytime
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= v
    if keys[pygame.K_RIGHT]:
        x += v
    if keys[pygame.K_UP]:
        y -= v
    if keys[pygame.K_DOWN]:
        y += v

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, h, w))
    pygame.display.update()

# uninitialize pygame
# pygame closes automatically when interpreter stops
pygame.quit()
