#2609번 백준 실버5

from math import gcd

n,m = map(int,input().split())

print(gcd(n,m))
print(n*m//gcd(n,m))