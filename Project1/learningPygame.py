# Creating an empty screen that can be closed
import pygame
# initializing pygame
pygame.init()

# creating a screen
sh = 240
sw = 180
screen = pygame.display.set_mode((sh, sw))

# loading and setting logo and title
#logo = pygame.image.load("logo32x32.png")
#pygame.display.set_icon(logo)
pygame.display.set_caption("First pygame")

x = 50
y = 50
h = 20
w = 20
v = 5
isJump = False
T = 7
t = T

running = True
while running:
    pygame.time.delay(50)

    for event in pygame.event.get():
        # adding option to quit anytime
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x >= v:
        x -= v
    if keys[pygame.K_RIGHT] and x <= sh-w-v:
        x += v
    if not isJump:
        if keys[pygame.K_UP] and y >= v:
            y -= v
        if keys[pygame.K_DOWN] and y <= sw-h-v:
            y += v
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if t >= -T:
            y -= int(0.5*t*abs(t))
            t -= 1
        else:
            t = T
            isJump = False

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, h, w))
    pygame.display.update()

# uninitialize pygame
# pygame closes automatically when interpreter stops
pygame.quit()
