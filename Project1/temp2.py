def longestcommonsubsequence(a, b):
    lcs = []
    for i in range(len(a)):
        row = []
        for j in range(len(b)):
            row.append(0)
        lcs.append(row)
    i = 1
    j = 1
    if a[0] == b[0]:
        lcs[0][0] = 1
    while i < len(a):
        if lcs[i - 1][0] == 1:
            lcs[i][0] = 1
        elif a[i] == b[0]:
            lcs[i][0] = 1
        i += 1
    while j < len(b):
        if lcs[0][j - 1] == 1:
            lcs[0][j] = 1
        elif a[0] == b[j]:
            lcs[0][j] = 1
        j += 1
    i = 1
    j = 1
    while i < len(a):
        while j < len(b):
            if a[i] == b[j]:
                lcs[i][j] = 1 + lcs[i - 1][j - 1]
            else:
                lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])
            j += 1
        i += 1
        j = 1
    i = len(a) - 1
    j = len(b) - 1
    s = ''
    while i > 0 and j > 0:
        if lcs[i][j] == 0:
            break
        if lcs[i][j] == lcs[i][j - 1]:
            j = j - 1
        elif lcs[i][j] == lcs[i - 1][j]:
            i = i - 1
        else:
            s = s + a[i]
            i = i - 1
            j = j - 1
    if (i == 0 or j == 0) and i != j:
        if lcs[0][0] != lcs[i][j]:
            s = s + a[i]
    if lcs[0][0] == 1:
        s = s + a[0]
    return s[::-1]


print(longestcommonsubsequence('abazdc', 'bacbad'))
print(longestcommonsubsequence('abcdaf', 'acbcf'))
print(longestcommonsubsequence('abcdef', 'xyzabc'))
