#백준 2231 분해합

n = int(input())
ans = 0

for i in range(1, n+1):
    data = list(map(int,str(i)))
    ans = i +sum(data)
    if ans == n :
        print(i)
        break
    if n ==i :
        print(0)