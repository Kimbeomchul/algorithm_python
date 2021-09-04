from collections import deque
n = int(input())
sand = deque()
command = []
for _ in range(n):
    sand.append(deque(map(int,input().split())))

m = int(input())
for _ in range(m):
    command.append(list(map(int,input().split())))

for c in command:
    if c[1] == 0:
        for i in range(c[2]):
            temp = sand[c[0]-1].popleft()
            sand[c[0]-1].append(temp)
    else:
        for i in range(c[2]):
            temp = sand[c[0]-1].pop()
            sand[c[0]-1].appendleft(temp)

ans = 0
for i in range(n//2):
    sand[i] = list(sand[i])
    sand[-(i+1)] = list(sand[-(i+1)])

    ans += sum(sand[i][0+i : n-i])
    ans += sum(sand[-(i+1)][0+i : n-i])
sand[n//2] = list(sand[n//2])
ans += sand[n//2][n//2]
print(ans)
