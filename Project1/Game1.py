import pygame
pygame.init()

sh = 500
sw = 500
win = pygame.display.set_mode((sw, sh))

h = int(sh/5)
w = 10
x1 = 0
y1 = int((sh-h)/2)
x2 = sw-w
y2 = int((sh-h)/2)
x = int(sw/2)-10
y = int(sh/2)
r = int(min(sh, sw)/50)
v = 5
ux = 5
uy = 5

running = True
while running:
    pygame.time.delay(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and y1 >= v:
        y1 -= v
    if keys[pygame.K_s] and y1 <= sh-h-v:
        y1 += v

    if keys[pygame.K_UP] and y2 >= v:
        y2 -= v
    if keys[pygame.K_DOWN] and y2 <= sh-h-v:
        y2 += v

    if x+r+ux > x2 and y2 <= y+uy <= y2+h:
        ux = -ux
    elif x-r+ux < x1+w and y1 <= y+uy <= y1+h:
        ux = -ux
    elif x+r+ux > sw:
        ux = -ux
    elif x-r+ux < 0:
        ux = -ux
    if y-r+uy < 0:
        uy = -uy
    elif y+r+uy > sh:
        uy = -uy

    x += ux
    y += uy
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), (x1, y1, w, h))
    pygame.draw.rect(win, (255, 255, 255), (x2, y2, w, h))
    pygame.draw.circle(win, (255, 255, 255), (x, y), r, 1)
    pygame.display.update()

pygame.quit()