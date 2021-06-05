# 백준 1929 소수구하기
import math
n, m = map(int,input().split())
data = [True for _ in range(m+1)]

for i in range(2, int(math.sqrt(m))+1):
    if data[i] == True:
        x = 2
        while i * x <= m:
            data[i*x] = False
            x += 1


for a in range(n):
    data[a] = False
for j in range(2,m+1):
    if data[j]:
        print(j)
