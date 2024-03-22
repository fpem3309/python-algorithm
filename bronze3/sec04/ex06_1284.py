# 0 = 4, 1 = 2, 나머지 = 3, 경계 = 1

size = [4, 2, 3, 3, 3, 3, 3, 3, 3, 3]
while True:
    num = input()
    result = len(num) + 1

    if int(num) == 0:
        break

    for i in num:
        index = int(i)
        result += size[index]

    print(result)
