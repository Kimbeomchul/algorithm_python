#백준 2659 십자카드문제 한국정보올림피아드 기출문제

# 코드가 더러어 ㅠ 뷁

from collections import deque

n = list(map(int,input().split()))
queue = deque()
min = 10000
count = 0
for i in n:
    queue.append(i)


for i in range(4):
    temp = str(queue[0]) + str(queue[1]) + str(queue[2]) + str(queue[3])
    temp = int(temp)
    if min > temp:
        min = temp

    a = queue.popleft()
    queue.append(a)

def sigaesu(i):
    min = 10000
    queue1 = deque()
    strs = str(i)
    queue1.append(strs[0])
    queue1.append(strs[1])
    queue1.append(strs[2])
    queue1.append(strs[3])

    for z in range(4):
        temp = queue1[0] + queue1[1] + queue1[2] + queue1[3]
        temp = int(temp)
        if min > temp:
            min = temp
        a = queue1.popleft()
        queue1.append(a)
    if min == i:
        return True

for i in range(1111,min):

    if sigaesu(i):
        count += 1

print(count+1)