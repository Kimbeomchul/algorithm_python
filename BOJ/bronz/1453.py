#백준 1453 피시방알바

n = int(input())
count = 0
data = list(map(int,input().split()))
data.sort()

for i in range(1,len(data)):
    if data[i] == data[i-1]:
        count += 1
    else:
        continue
print(count)
