n = int(input())
pan = []
sum_list = []
for _ in range(n):
    temp = list(map(int,input().split()))
    pan.append(temp)
    sum_list.append(sum(temp))

sum_daegak = 0
sum_daegak2 = 0
for i in range(n):
    sum_col = 0
    sum_daegak += pan[i][i]
    sum_daegak2 += pan[-i][-i]
    for j in range(n):
        sum_col += pan[j][i]
    sum_list.append(sum_col)

sum_list.append(sum_daegak)
sum_list.append(sum_daegak2)


print(max(sum_list))
