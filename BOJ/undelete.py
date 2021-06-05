#ATM 인하은행 백준 11399 실버3


n = int(input())

data = list(map(int,input().split()))
data.sort()
temp = data[0]
result = 0
for i in range(1,len(data)):
    if i == 1:
        data[i] += temp
        continue
    if i < len(data):
        data[i] = data[i] + data[i-1]
    else:
        data[i] = data[i] + data[i-1]

for a in data:
    result += a
print(result)