n = int(input())
m = [input() for _ in range(n)]

for idx,i in enumerate(m):
    i = i.upper()
    if i == i[::-1]:
        print("#" + str(idx+1) + " YES")
    else:
        print("#" + str(idx+1) + " NO")
