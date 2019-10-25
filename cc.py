def gridSearch(G, P):
    b = True
    for i in range(R - r + 1):
        for j in range(C - c + 1):
            for k in range(r):
                if G[i + k][j:j + c] != P[k]:
                    b = False
                    break
            if b is True:
                return 'YES'
            else:
                b = True
    if b is True:
        return 'NO'


R = 10
C = 10
r = 3
c = 4
G = ['7283455864', '6731158619', '8988242643', '3830589324', '2229505813', '5633845374', '6473530293', '7053106601',
     '0834282956', '4607924137']
P = ['9505', '3845', '3530']
print(gridSearch(G, P))
print(G[4][3:3 + 4], P[0])
