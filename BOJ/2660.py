#백준 2660 회장뽑기 한국정보올림피아드
#실패

from collections import deque
n = int(input())
datas = [[0 for _ in range(n+1)]for _ in range(n+1)]
while True:
    x, y = map(int,input().split())
    if x == -1 and y == -1:
        break
    datas[x][y] = 1
    datas[y][x] = 1

maxs = 0
idx = []
for i in range(len(datas)):
    if maxs <= sum(datas[i]):
        maxs = sum(datas[i])

for j in range(len(datas)):
    if sum(datas[j]) ==  maxs:
        idx.append(j)

tmp = maxs-1
temp = str(tmp) + ' ' + str(maxs)
print(temp)
for i in idx:
    print(i,end=' ')