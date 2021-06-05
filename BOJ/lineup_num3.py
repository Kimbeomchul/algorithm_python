#10989번 라인업3 백준 실버5

import sys
input = sys.stdin.readline
data = int(input())
count = [0 for _ in range(10000)]
for i in range(data):
    count[int(input())-1] += 1
print(count)
for j in range(len(count)):
    for z in range(count[j]):
        print(j+1)