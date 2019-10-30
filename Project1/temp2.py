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
    s = []
    while i > 0 and j > 0:
        if lcs[i][j] == 0:
            break
        if lcs[i][j] == lcs[i][j - 1]:
            j = j - 1
        elif lcs[i][j] == lcs[i - 1][j]:
            i = i - 1
        else:
            s.append(a[i])
            i = i - 1
            j = j - 1
    if lcs[i][j] == 1:
        if j == 0 and i != 0:
            while i >= 0:
                if lcs[i][0] == 0:
                    s.append(a[i + 1])
                    break
                i = i - 1
        elif i == 0 and j != 0:
            while j >= 0:
                if lcs[0][j] == 0:
                    s.append(b[j + 1])
                    break
                j = j - 1
        else:
            s.append(a[0])
    return s[::-1]


print(longestcommonsubsequence('abazdc', 'bacbad'))
print(longestcommonsubsequence('abcdaf', 'acbcf'))
print(longestcommonsubsequence('abcdef', 'xyzabc'))
a = [16, 27, 89, 79, 60, 76, 24, 88, 55, 94, 57, 42, 56, 74, 24, 95, 55, 33, 69, 29, 14, 7, 94, 41, 8, 71, 12, 15, 43,
     3, 23, 49, 84, 78, 73, 63, 5, 46, 98, 26, 40, 76, 41, 89, 24, 20, 68, 14, 88, 26]
b = [27, 76, 88, 0, 55, 99, 94, 70, 34, 42, 31, 47, 56, 74, 69, 46, 93, 88, 89, 7, 94, 41, 68, 37, 8, 71, 57, 15, 43,
     89, 43, 3, 23, 35, 49, 38, 84, 98, 47, 89, 73, 24, 20, 14, 88, 75]
print(longestcommonsubsequence(a, b))
