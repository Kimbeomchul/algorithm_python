n = int(input())
data = list(map(int,input().split()))
res = int(round(sum(data)/n))
min = 999999
save = 0
for idx,i in enumerate(data):
    if abs(res - i) < min:
        min = abs(res - i)
        ros = i
        save = idx + 1
    elif abs(res-i) == min:
        if i > ros:
            ros = i
            save = idx + 1

print(res,save)