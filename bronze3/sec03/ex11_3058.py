t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    sum = 0
    min_v = 101
    for j in range(7):
        if a[j] % 2 == 0:
            sum += a[j]
            if a[j] < min_v:
                min_v = a[j]

    print(str(sum) + " " + str(min_v))
