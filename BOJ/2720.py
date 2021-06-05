# 백준 2720 세탁소 사장 동혁

n = int(input())
datas = []
change = [25,10,5,1]
res = []
dt = ''
for i in range(n):
    datas.append(int(input()))



for data in datas:
    for x in change:
        temp = 0
        if data >= x:
            temp += data//x
            data = data % x
            dt += str(temp) + ' '
        else:
            dt += str(0) + ' '
    res.append(dt)
    dt = ''
for j in res:
    print(j)

