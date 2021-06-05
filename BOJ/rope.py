#백준 2217번 로프

n  = int(input())
data =[]
for i in range(n):
    data.append(int(input()))

data.sort()
res = data[0] * n
print(res)
