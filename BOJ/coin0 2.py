#코인0 백준 11047번 실버2

n , m = map(int,input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
ans = 0
for a in coin:
    if int(a) <= m:
        ans += m // int(a)
        m = m % int(a)
print(ans)
