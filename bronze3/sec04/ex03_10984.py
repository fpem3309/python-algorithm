t = int(input())
for i in range(t):
    n = int(input())
    a, b = 0, 0
    for j in range(n):
        c, g = map(float, input().split())
        a += c
        b += c * g
    print("%d %.1f" %(a, b / a))
