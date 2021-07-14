from itertools import combinations

n, k = map(int,input().split())
data = list(combinations((map(int,input().split())),3))
datas = []

for i in data:
    datas.append(sum(i))
datas.sort(reverse=True)

print(datas[k-1])
