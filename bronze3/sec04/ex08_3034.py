n, w, h = map(int, input().split())
size = w * w + h * h
for i in range(n):
    m = int(input())
    if m <= size ** (1 / 2):
        print("DA")
    else:
        print("NE")
