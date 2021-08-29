n = int(input())
ans = [False,False] + [True] * n
counter = 0
for i in range(2, n):
    if ans[i]:
        for j in range(i+i,n,i):
            ans[j] = False
        counter += 1
print(counter)
