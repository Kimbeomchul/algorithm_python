n = int(input())
maps = [[0] * (n+2)]
for _ in range(n):
    maps.append([0] + list(map(int, input().split())) + [0])

maps.append([0] * (n+2))

answer = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if maps[i][j] > maps[i][j+1] and maps[i][j] > maps[i][j-1] and maps[i][j] > maps[i+1][j] and maps[i][j] > maps[i-1][j]:
            answer += 1

print(answer)

