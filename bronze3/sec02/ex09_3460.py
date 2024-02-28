import sys

input = sys.stdin.readline
print = sys.stdout.write

t = int(input())
a = []

for i in range(t):
    n = int(input())
    index = 0
    while n > 0:
        if n % 2 == 1:
            a.append(index)
        n //= 2
        index += 1

for j in a:
    print(str(j)+" ")