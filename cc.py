N = int(input(""))
edge = {str(i+1): [] for i in range(N)}
for i in range(N - 1):
    x, y = str(input("")).split()
    edge[x].append(y)
    edge[y].append(x)
vertexValue = list(map(int, input("").split()))
path = []


def dfs(a, total,  pth, dnt):
    global paths, path
    for i in edge[a]:
        if i not in dnt[a] and i not in pth:
            pth.append(i)
            dnt[a].add(i)
            for t in pth:
                total += vertexValue[int(t)-1]
            return dfs(i, total, pth, dnt)
    path.append(total)
    try:
        for t in pth:
            total -= vertexValue[int(t) - 1]
        del pth[-1]
        dfs(pth[-1], total, pth, dnt)
    except IndexError:
        return


for i in range(1, N+1):
    a = str(i)
    pth = [a]
    total = vertexValue[int(a) - 1]
    dnt = {str(_): set() for _ in range(1, N + 1)}
    dfs(a, total, pth, dnt)
print(max(path))