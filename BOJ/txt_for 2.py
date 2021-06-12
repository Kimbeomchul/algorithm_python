# 문자열반복 브론즈2
n = int(input())
for a in range(n):
    temp = ''

    x,y = input().split()
    x = int(x)
    for i in range(len(y)):
        temp += y[i] * x
    print(temp)