h, w = map(int, input().split())
n = int(input())
a = [[0 for j in range(w)] for i in range(h)]

for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(l):
            # if j < w:
            a[x - 1][j + y - 1] = 1
    elif d == 1:
        for j in range(l):
            # if j < h:
            a[x + j - 1][y - 1] = 1

for i in range(h):
    for j in range(w):
        print(a[i][j], end=' ')
    print()