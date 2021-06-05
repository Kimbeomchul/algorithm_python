# 백준 16453 스네이크버드

n , m = list(map(int,input().split()))
data = list(map(int,input().split()))
data.sort()
for i in range(len(data)):
    if data[i] <= m:
        m = m+1
    elif data[i] > m:
        break
print(m)