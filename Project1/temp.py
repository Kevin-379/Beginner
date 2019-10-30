# sets are very, very fast for finding element in it w.r.t list. (>10sec to <0.3sec)
def weightedUniformStrings(s, queries):
    su = set()
    prev = -1
    length = 1
    for c in s:
        w = ord(c)-ord('a')+1
        if c != prev:
            su.add(w)
            length = 1
        else:
            length += 1
            su.add(w*length)
        prev = c
    t = []
    for i in queries:
        if i in su:
            t.append('Yes')
        else:
            t.append('No')
    return t


print(weightedUniformStrings('abbc', [5, 1, 4, 3]))
print(weightedUniformStrings('ahasfaa', [5, 19, 6, 1, 2]))

s=set()
