
def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = int(f)
        f *= i
        f = str(f)
        l = len(f)
        last, cnt = 0, 0
        for j in range(l-1, 0, -1):
            if f[j] != '0':
                last = cnt
                break
            cnt += 1
        f = f[:l-last]
        l = len(f)
        if l > 5:
            f = f[-9:]
    return f[-5:]

n = int(input())
lists = []
print(fact(n))


#
import math
# temp = math.factorial(n)
# temp = str(temp)
# n = len(temp)
# last, cnt = 0, 0
# for i in range(n-1, 0, -1):
#     if temp[i] != '0':
#         last = cnt
#         break
#     cnt += 1
# print(temp[n-last-5:n-last])
# for i in temp:
#     lists.append(i)
# print(lists)
#
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