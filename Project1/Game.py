from os import system, name
from time import sleep


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


#print("Hello World\n"*10)
#sleep(2)
#clear()

R = 9
C = 20

a = [[" " for i in range(C)] for j in range(R)]
a[3][0] = "|"
a[4][0] = "|"
a[5][0] = "|"
a[3][-1] = "|"
a[4][-1] = "|"
a[5][-1] = "|"

x = 4
y = 1
u = 1
v = 1
a[x][y] = "O"

A = 0
B = 0

for i in range(R):
    a[i].insert(0, "|")
    a[i].append("|")
    print("".join(a[i]))
print("")
y += 1
C += 2

for i in range(100):
    a[x][y] = " "
    if x+u >= R:
        u = -u
    elif x+u < 0:
        u = -u
    if a[x+u][y+v] == "|" and y+v == C-2:
        B += 1
    if a[x+u][y+v] == "|" and y+v == 1:
        A += 1
    if a[x+u][y+v] == "|":
        v = -v
    if x+2*u == -1 or x+2*u == R or x-u == -1 or x-u == R:
        pass
    else:
        a[x-u][-2] = " "
        a[x+2*u][-2] = "|"
    x = x+u
    y = y+v
    a[x][y] = "O"
    for i in range(R):
        print("".join(a[i]))
    print(A, B)
    sleep(0.2)
    clear()
