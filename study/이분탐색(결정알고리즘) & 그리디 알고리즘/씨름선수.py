n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

data = sorted(data, key= lambda x: x[0])

counter = 0

for i in range(n):
    for j in range(i+1,n):
        if data[i][1] < data[j][1]:
            break
    else:
        counter += 1
print(counter)
