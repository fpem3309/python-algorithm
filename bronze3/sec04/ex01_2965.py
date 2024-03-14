a, b, c = map(int, input().split())
case1 = b - a - 1
case2 = c - b - 1
print(max(case1, case2))