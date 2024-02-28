import sys

input = sys.stdin.readline

Max = 0
Sum = 0
for i in range(10):
    a, b = map(int, input().split())
    Sum += (b - a)
    if Sum > Max:
        Max = Sum
print(Max)