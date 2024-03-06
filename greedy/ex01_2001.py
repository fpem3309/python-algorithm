maxA = maxB = 2000
for i in range(3):
    x = int(input())
    if x < maxA: maxA = x
for i in range(2):
    x = int(input())
    if x < maxB: maxB = x
print(maxA + maxB + ((maxA + maxB) * 0.1))
