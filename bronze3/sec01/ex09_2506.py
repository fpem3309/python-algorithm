import sys

input = sys.stdin.readline

Sum = 0
count = 0
n = int(input())
x = list(map(int, input().split()))

for i in range(n):
    if x[i] == 1:
        count += 1
        Sum += count
    else:
        count = 0
print(Sum)
