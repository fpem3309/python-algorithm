import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
team = 0
while True:
    if (n-2) + (m-1) < k or n < 2 or m < 1:
        break

    if n >= 2 and m >= 1:
        team += 1
        n -= 2
        m -= 1

print(team)