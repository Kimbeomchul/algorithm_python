#백준 7576 토마토

from collections import deque

n , m = map(int,input().split())
tomato = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
res = 0

queue= deque()
for i in range(m):
    tomato.append(list(map(int,input().split())))
    for j in range(n):
        if tomato[i][j] == 1:
            queue.append([i,j])

while queue:
    x , y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 > nx or 0 > ny or nx >= m or ny >= n:
            continue

        if tomato[nx][ny] == 0:
            tomato[nx][ny] = tomato[x][y] +1
            queue.append([nx,ny])
temp = -99
temp2 = 0
for i in tomato:
    for j in i:
        if j == 0:
            temp2 = 1
        else:
            res = max(temp,j)
            temp = res


if temp2 == 1:
    print(-1)
elif res == 1:
    print(0)
else:
    print(res-1)

