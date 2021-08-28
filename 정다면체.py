from collections import Counter
n,m = map(int,input().split())
data = []
ans = []
for i in range(1,n+1):
    for j in range(1,m+1):
        data.append(i+j)
temp = Counter(data)
max_data = max(temp.values())
for i,j in temp.items():
    if j == max_data:
        ans.append(i)

print(ans)
