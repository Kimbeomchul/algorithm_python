#백준 4673번 실버5
data = []

def cons(n):
    x = 0
    for i in list(str(n)):
        x = x + int(i)
    return int(n) + x

for j in range(1,10001):
    datas = cons(j)
    data.append(datas)

for z in range(1, 10001):
    if z in data:
        pass
    else:
        print(z)