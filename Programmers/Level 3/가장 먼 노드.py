from collections import deque

def BFS(root,visited,data,idx):
    queue = deque()
    queue.append(root)

    visited[root] = True

    while queue:
        x = queue.popleft()

        for i in data[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                idx[i] = idx[x] + 1

    return idx.count(max(idx))

def solution(n, edge):
    idx = [0 for _ in range(n+1)]

    visited = [False] * (n+1)
    data = [[] for _ in range(n+1)]

    for i in edge:
        data[i[0]].append(i[1])
        data[i[1]].append(i[0])


    return BFS(1,visited,data,idx)