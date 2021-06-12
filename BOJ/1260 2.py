# 백준 1260 DFS BFS
from collections import deque


def DFS(data, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in data:
                temp = list(set(data[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return ' '.join(str(i) for i in visited)


def BFS(data, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in data:
                temp = list(set(data[n]) - set(visited))
                temp.sort()
                queue += temp
    return ' '.join(str(i) for i in visited)

data = {}
n, m, v = map(int, input().split())

for _ in range(m):
    x, y = map(int,input().split())
    if x not in data:
        data[x] = [y]
    elif y not in data[x]:
        data[x].append(y)

    if y not in data:
        data[y] = [x]
    elif x not in data[y]:
        data[y].append(x)

print(DFS(data,v))
print(BFS(data,v))

