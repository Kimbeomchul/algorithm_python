#print((lambda x: int(x[0])-int(x[1]))(input().split()))
#
# n = list(input().split())
# print(len(n))
#


import math

n = int(input())
temp = math.factorial(n)
temp = str(temp)
lists= []

n = len(temp)
last, cnt = 0, 0
for i in range(n-1, 0, -1):
    if temp[i] != '0':
        last = cnt
        break
    cnt += 1
print(temp[n-last-5:n-last])
# for i in temp:
#     lists.append(i)
# print(lists)

# ans = []
# for a in range(len(lists)-1, 0 , -1):
#     if len(ans) == 5:
#         break
#     if lists[a] != '0' and len(ans) < 2:
#         ans += lists[a]
#     elif len(ans) > 1:
#         ans += lists[a]
# temps = ''
# for x in range(len(ans),0,-1):
#      temps += ans[x-1]
# print(temps)