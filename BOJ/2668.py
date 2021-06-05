#백준 2668 한국정보올림피아드 기출


n = int(input())
data = {}
count = 0
for i in range(1,n+1):
    data[i] = int(input())

while True:
    for_del = []
    temp = set(data.values())
    for i in data.items():
        if i[0] not in temp:
            for_del.append(i[0])

    for j in for_del:
        data.pop(j)
    temp2 = set(data.values())
    count += 1
    if temp == temp2:
        break
print(len(data))

for i in data.keys():
    print(i)