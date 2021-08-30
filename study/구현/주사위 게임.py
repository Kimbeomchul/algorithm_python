n = int(input())
m = []
money = []
for _ in range(n):
    m.append(input().split())

for i,j,k in m:
    if i == j == k:
        money.append(10000 + int(i) * 1000)
    elif i == j or i == k:
        money.append(1000 + int(i) * 100)
    elif j == k:
        money.append(1000 + int(j) * 100)
    else:
        money.append(int(max(i,j,k)) * 100)

print(max(money))
