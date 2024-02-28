import sys
input = sys.stdin.readline

n = int(input())
Sum = 0
for i in range(n):
    Sum += int(input())

print(Sum - (n - 1))