import sys

input = sys.stdin.readline

prize1 = [0, 500, 300, 300, 200, 200, 200, 50, 50, 50, 50,
          30, 30, 30, 30, 30, 10, 10, 10, 10, 10, 10]
prize2 = [0, 512, 256, 256, 128, 128, 128, 128, 64, 64, 64, 64, 64, 64, 64, 64,
          32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32]

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    if a > 21:
        a = 0
    if b > 31:
        b = 0

    print((prize1[a]+prize2[b])*10000)
