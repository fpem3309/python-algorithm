d = [[0 for j in range(20)] for i in range(20)]
for i in range(19):
    d[i] = list(map(int, input().split()))

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    for j in range(19):
        if d[x][j] == 1:
            d[x][j] = 0
        else:
            d[x][j] = 1

        if d[j][y] == 1:
            d[j][y] = 0
        else:
            d[j][y] = 1

for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()