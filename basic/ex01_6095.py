d = [[0 for j in range(20)] for i in range(20)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    d[x-1][y-1] = 1

for i in range(20):
    for j in range(20):
        print(d[i][j], end=' ')
    print()