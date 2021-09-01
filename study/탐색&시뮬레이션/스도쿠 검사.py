sdocu = []
for _ in range(9):
    sdocu.append(list(map(int,input().split())))

idx = 0
idx2 = 3

x = 0
while True:
    temp = []
    for i in range(3):
        temp += sdocu[x][idx:idx2]
        x += 1

    temp.sort()
    if [1,2,3,4,5,6,7,8,9] != temp:
        print("NO")
        break

    if x == 9:
        if idx2 == 9:
            print("YES")
            break
        else:
            x = 0
            idx += 3
            idx2 += 3


