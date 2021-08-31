data = []
for _ in range(2):
    x = int(input())
    data.append(list(map(int,input().split())))
answer = []
for i in data:
    for j in i:
        answer.append(j)
answer.sort()
print(answer)
