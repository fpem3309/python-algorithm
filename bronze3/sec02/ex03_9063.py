import sys
input = sys.stdin.readline

n = int(input())
max_x, max_y, min_x, min_y = -10000, -10000, 10000, 10000

for i in range(n):
    x, y = map(int, input().split())
    if x < min_x: min_x = x
    if x > max_x: max_x = x
    if y < min_y: min_y = y
    if y > max_y: max_y = y

print((max_x - min_x) * (max_y - min_y))
