import sys

input = sys.stdin.readline

t = int(input())
c, s = 100, 100
for i in range(t):
    a, b = map(int, input().split())
    if a > b:
        s -= a
    elif a < b:
        c -= b

print(c)
print(s)