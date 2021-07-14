
n , k = map(int,input().split())
data = []
cnt = 0
for i in range(1,n+1):
    if cnt == k:
        break
    if n % i == 0:
        cnt += 1
print(cnt)


