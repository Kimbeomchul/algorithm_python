#백준 15552 빠른 A+B

import sys
a = int(sys.stdin.readline())

for _ in range(a):
    x, y = map(int,sys.stdin.readline().split())
    print(x+y)