#백준 1644 소수이 연속합

import math
n = int(input())
data = [True for _ in range(n+1)]
data[0] = False
data[1] = False
ans = []


for i in range(2,int(math.sqrt(n))+1):
    if data[i] == True:
        for j in range(i+i , n+1, i):
            data[j] = False

for j in range(len(data)):
    if data[j]:
        ans.append(j)

start = 0
count = 0
temp = 0
if n in ans:
    count += 1
while True:
    if start >= len(ans)-1:
        break
    for x in range(start , len(ans)):

        if temp == n:
            count += 1
            start += 1
            temp = 0
            break
        elif temp > n:
            start += 1
            temp = 0
            break
        temp += ans[x]

print(count)