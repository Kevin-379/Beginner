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
score1 = 0
score2 = 0
font = pygame.font.SysFont('comicsans', 30)

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

    V = True

    if x+r+ux > x2 and y2 <= y+uy <= y2+h:
        ux = -ux
    elif x-r+ux < x1+w and y1 <= y+uy <= y1+h:
        ux = -ux
    elif x+r+ux > x2:
        score1 += 1
        x1 = 0
        y1 = int((sh - h) / 2)
        x2 = sw - w
        y2 = int((sh - h) / 2)
        x = int(sw / 2) - 10
        y = int(sh / 2)
        V = False
    elif x-r+ux < x1+w:
        score2 += 1
        x1 = 0
        y1 = int((sh - h) / 2)
        x2 = sw - w
        y2 = int((sh - h) / 2)
        x = int(sw / 2) - 10
        y = int(sh / 2)
        V = False
    if y-r+uy < 0 and V:
        uy = -uy
    elif y+r+uy > sh and V:
        uy = -uy


    x += ux
    y += uy
    win.fill((0, 0, 0))
    text1 = font.render(str(score1), 1, (255, 0, 0))
    text2 = font.render(str(score2), 1, (255, 0, 0))
    win.blit(text1, (100, 0))
    win.blit(text2, (400, 0))
    pygame.draw.rect(win, (255, 255, 255), (x1, y1, w, h))
    pygame.draw.rect(win, (255, 255, 255), (x2, y2, w, h))
    pygame.draw.circle(win, (255, 255, 255), (x, y), r, 1)
    pygame.display.update()
    if not V:
        pygame.time.delay(1000)
        V = True
        ux = -ux

pygame.quit()