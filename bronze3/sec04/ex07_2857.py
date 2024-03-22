notFind = True
for i in range(1, 6):
    name = input()
    if "FBI" in name:
        notFind = False
        print(i, end=" ")

if notFind:
    print("HE GOT AWAY!")
