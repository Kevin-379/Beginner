import pygame
import random

sh = 400
sw = 400
h = 80
w = 80
b = []
for i in range(0, sw, w):
    for j in range(0, sh, h):
        b.append((i, j))


v = [0 for i in range(25)]

r = random.sample(range(25), 5)
for i in range(5):
    v[r[i]] = None

if v[0] is None:
    if v[1] is not None:
        v[1] += 1
    if v[5] is not None:
        v[5] += 1
    if v[6] is not None:
        v[6] += 1
if v[4] is None:
    if v[3] is not None:
        v[3] += 1
    if v[9] is not None:
        v[9] += 1
    if v[8] is not None:
        v[8] += 1
if v[20] is None:
    if v[21] is not None:
        v[21] += 1
    if v[15] is not None:
        v[15] += 1
    if v[16] is not None:
        v[16] += 1
if v[24] is None:
    if v[23] is not None:
        v[23] += 1
    if v[19] is not None:
        v[19] += 1
    if v[18] is not None:
        v[18] += 1
for i in [1, 2, 3]:
    if v[i] is None:
        if v[i-1] is not None:
            v[i-1] += 1
        if v[i+1] is not None:
            v[i+1] += 1
        if v[i+5] is not None:
            v[i+5] += 1
        if v[i+4] is not None:
            v[i+4] += 1
        if v[i+6] is not None:
            v[i+6] += 1
for i in [5, 10, 15]:
    if v[i] is None:
        if v[i-5] is not None:
            v[i-5] += 1
        if v[i+1] is not None:
            v[i+1] += 1
        if v[i+5] is not None:
            v[i+5] += 1
        if v[i-4] is not None:
            v[i-4] += 1
        if v[i+6] is not None:
            v[i+6] += 1
for i in [9, 14, 19]:
    if v[i] is None:
        if v[i-1] is not None:
            v[i-1] += 1
        if v[i-5] is not None:
            v[i-5] += 1
        if v[i+5] is not None:
            v[i+5] += 1
        if v[i+4] is not None:
            v[i+4] += 1
        if v[i-6] is not None:
            v[i-6] += 1
for i in [21, 22, 23]:
    if v[i] is None:
        if v[i-1] is not None:
            v[i-1] += 1
        if v[i+1] is not None:
            v[i+1] += 1
        if v[i-5] is not None:
            v[i-5] += 1
        if v[i-4] is not None:
            v[i-4] += 1
        if v[i-6] is not None:
            v[i-6] += 1
for i in [6, 7, 8, 11, 12, 13, 16, 17, 18]:
    if v[i] is None:
        if v[i-1] is not None:
            v[i-1] += 1
        if v[i+1] is not None:
            v[i+1] += 1
        if v[i+5] is not None:
            v[i+5] += 1
        if v[i+4] is not None:
            v[i+4] += 1
        if v[i+6] is not None:
            v[i+6] += 1
        if v[i-5] is not None:
            v[i-5] += 1
        if v[i-4] is not None:
            v[i-4] += 1
        if v[i-6] is not None:
            v[i-6] += 1

pygame.init()


win = pygame.display.set_mode((sw, sh))
font = pygame.font.SysFont('comicsans', 50)
running = True
a = []
while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for i in range(0, sw, w):
                for j in range(0, sh, h):
                    if i <= pos[0] <= i+w and j <= pos[1] <= j+w:
                        if v[int(i/w + 5*j/h)] is None:
                            pygame.time.delay(1000)
                            running = False
                        else:
                            a.append(((font.render(str(v[int(i/w + 5*j/h)]), 1, (255, 0, 0))), (i+int(w/4), j+int(h/4))))

    win.fill((160, 160, 160))
    for i in range(25):
        pygame.draw.rect(win, (80, 80, 80), (b[i][0], b[i][1], h, w), 10)
    for s in a:
        win.blit(s[0], s[1])
    pygame.display.update()

pygame.quit()
print(v)