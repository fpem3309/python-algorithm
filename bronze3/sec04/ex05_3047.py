abc = list(map(int, input().split()))
abc.sort()

od = input()
for i in od:
    if i == 'A':
        print(abc[0], end=' ')
    elif i == 'B':
        print(abc[1], end=' ')
    else:
        print(abc[2], end=' ')
