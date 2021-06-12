#백준 2693 N번째 큰 수

n = int(input())
data =[]
res = []
for i in range(n):
    data.append(list(map(int,input().split())))
    data[i].sort(reverse=True)
    res.append(data[i][2])

for j in res:
    print(j)