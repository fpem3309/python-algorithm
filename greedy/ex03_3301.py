m = int(input())
cnt = 0
case = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for i in case:
    cnt += m // i
    m -= i * (m // i)
print(cnt)