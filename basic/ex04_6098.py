miro = [[] for i in range(10)]
for i in range(10):
    miro[i] = list(map(int, input().split()))

i = 1
j = 1
while True:

    if miro[i][j] == 0:
        miro[i][j] = 9
        if miro[i][j + 1] == 1:
            i += 1
        elif miro[i][j + 1] == 0:
            j += 1
        else:
            miro[i][j+1] = 9
            break
    else:
        break

    if miro[i][j] == 2:
        miro[i][j] = 9
        break


for i in range(10):
    for j in range(10):
        print(miro[i][j], end=' ')
    print()
