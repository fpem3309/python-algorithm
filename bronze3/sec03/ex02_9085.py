import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    Sum = 0
    temp = list(map(int, input().split()))

    for j in range(n):
        Sum += temp[j]
    print(Sum)