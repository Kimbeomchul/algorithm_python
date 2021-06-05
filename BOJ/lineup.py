#백준 2252번 골드 2  줄세우기

from itertools import combinations
n , m = map(int,input().split())
lists = []
data = []



for i in range(m):
    lists.append(input().split())
    data += lists[i]

data = list(combinations(data, 3))
print(data)
# if len(data) > n:
#     res = set(data)
#     res = list(res)
#
#
# res.sort()
# print(res)