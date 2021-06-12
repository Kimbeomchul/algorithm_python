#백준 4539 반올림
n = int(input())

for _ in range(n):
    x = int(input())
    temp = str(x)
    temp2 = len(temp)
    if temp2 == 1:
        x = x
    elif temp2 == 2:
        x = round(x,-1)
    else:
        for i in range(1,temp2):
            a = 10 ** (i-1)
            x += a
            x = round(x,-i)

    print(x)
