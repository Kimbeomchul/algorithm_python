#백준 11724 연결요소의 개수

import sys
sys.setrecursionlimit(10000)

count = 0
n , m = map(int,input().split())
data = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    x,y = map(int,input().split())
    data[x].append(y)
    data[y].append(x)

def DFS(i):
    visited[i] = True
    for x in data[i]:
        if not visited[x]:
            DFS(x)

for i in range(1,n+1):
    print(visited)
    if not visited[i]:
        DFS(i)
        count += 1

print(count)
