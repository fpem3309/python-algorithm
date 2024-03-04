import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

for i in range(n):
    for j in range(n + i):
        if j == n - i - 1 or j == n + i - 1:
            print("*")
        else:
            print(" ")
    print("\n")