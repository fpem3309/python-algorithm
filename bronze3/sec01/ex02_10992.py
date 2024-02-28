import sys

print = sys.stdout.write
n = int(input())

for i in range(n):
    for j in range(n + i):
        if i == 0:
            if j == n - 1:
                print("*")
            else:
                print(" ")
        elif i != n - 1:
            if j == n - 1 - i or j == n - 1 + i:
                print("*")
            else:
                print(" ")
        else:
            print("*")
    print("\n")