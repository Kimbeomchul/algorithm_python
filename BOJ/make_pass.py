#암호만들기 백준 1759번 골드 5
from itertools import combinations
n , m = map(int,input().split())
data = input().split()
data.sort()
comb = list(combinations(data,n))
for i in comb:
    ja = 0
    mo = 0
    for j in i:
        if j in 'aeiou':
            ja += 1
        else:
            mo += 1
    if ja >= 1 and mo >= 2:
        print(''.join(i))