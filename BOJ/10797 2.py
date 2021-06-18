# 백준 10797 10부제 한국정보올림피아드

n = int(input())
data = list(map(int,input().split()))
count = 0
for _ in range(len(data)):
    if n in data:
        count += 1
        data.remove(n)
print(count)