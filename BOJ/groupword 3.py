#백준 1316번 실버5
data = []
count = 0
temps = 0
n = int(input())
for i in range(n):
    data.append(input())
for j in data:
    if temps == 1:
        count -= 1
    temps = 0
    count += 1
    temp = []
    for z in range(len(j)):
        if j[z] not in temp:
            temp.append(j[z])
        elif j[z] in temp:
            if j[z-1] == j[z]:
                pass
            else:
                temps = 1

if temps == 1:
    count -= 1
print(count)
