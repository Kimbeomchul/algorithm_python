def changes(pans):
    answer = 0
    idx = 0
    idx2 = 5
    x = 0
    for i in range(21):
        temp = pans[x][idx:idx2]
        if temp[::-1] == temp:
            answer += 1
        idx += 1
        idx2 += 1
        if idx % 3 == 0:
            x += 1
            idx = 0
            idx2 = 5
    return answer

pans = []
pans2 = []
for _ in range(7):
    pans.append(list(map(int,input().split())))

for i in range(7):
    temp = []
    for j in pans:
        temp.append(j[i])
    pans2.append(temp)

ans = 0
ans += changes(pans)
ans += changes(pans2)
print(ans)


