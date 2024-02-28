import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

for i in range(n):
    for j in range(2*n-1 + i % 2):
        if (i+j) % 2 == 0:
            print("*")
        else:
            print(" ")
    print("\n")