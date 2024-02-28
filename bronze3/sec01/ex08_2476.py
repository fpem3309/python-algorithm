import sys

input = sys.stdin.readline

Max = 0
n = int(input())

for i in range(n):
    a, b, c = map(int, input().split())
    score = 0
    if a == b == c:
        score = 10000 + a * 1000
    elif a == b or b == c or a == c:
        if a == b:
            score = 1000 + a * 100
        else:
            score = 1000 + c * 100
    else:
        score = max(a, b, c) * 100

    if score > Max:
        Max = score

print(Max)