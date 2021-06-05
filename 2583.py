#백준 2583번 영역구하기
# 첫 두개좌표는 뒤집고 / 뒤에 두개좌표는 뒤집고 -1씩

import sys
sys.setrecursionlimit(10001)

x,y,z = map(int,input().split())
ans = []
res = []
count = 0
temp =0

def DFS(i,j):

    if i < 0 or i >= x or j < 0 or j >= y:
        return False
    if data[i][j] == 0:
        ans.append(1)
        data[i][j] = 1
        DFS(i+1 , j)
        DFS(i , j+1)
        DFS(i-1, j)
        DFS(i, j-1)
        return True
    return False


data = [[0 for _ in range(y)] for _ in range(x)]
for _ in range(z):
    w,q,r,e = map(int,input().split())

    for i in range(q,e):
        for j in range(w,r):
            data[i][j] = 1

for i in range(x):
    for j in range(y):
        if DFS(i,j):
            count += 1
            ans.append('/')

for i in ans:
    if i == '/':
        res.append(temp)
        temp = 0
    else:
        temp += 1
res.sort()
print(count)
for i in res:
    print(i, end=' ')