from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


s = str(input(""))
clear()
s = s.lower()
l = []
for a in s:
    l.append(a.lower())
h = [[" ", "_", "_", " ", "_", "_", " ", "_", "_"], ["|", " ", " ", " ", " ", " ", " ", " ", " ", "|", " "],
     ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
     ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]

w = ["_" for i in range(len(s))]

g = [[2, 9, "O"], [3, 9, "|"], [3, 8, "/"], [3, 10, "\\"], [4, 8, "/"], [4, 10, "\\"]]

for i in h:
    print("".join(i))
print(" ".join(w))

wrong = 0
right = 0
while wrong < 6 and right < len(s):
    c = str(input("Enter a guess: "))
    if c in l:
        t = l.index(c)
        w[t] = c
        l[t] = " "
        right += 1
    else:
        h[g[wrong][0]][g[wrong][1]] = g[wrong][2]
        wrong += 1
    clear()
    for i in h:
        print("".join(i))
    print(" ".join(w))

if wrong == 6:
    print("Correct answer: " + s)