n = int(input())
m = list(map(int,input().split()))
answer =  0
counter = 1
for i in m:
    if i == 1:
        answer += counter
        counter += 1
    else:
        counter = 1

print(answer)
