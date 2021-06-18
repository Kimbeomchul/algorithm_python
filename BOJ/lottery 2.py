# 로또 백준 6603번 실버2

from itertools import combinations

while True:
    n = list(map(int,input().split()))
    if n[0] == 0:
        break
    del n[0]
    n= list(combinations(n, 6))
    for i in n:
        for j in i:
            print(j, end=' ')
        print()
    print()
