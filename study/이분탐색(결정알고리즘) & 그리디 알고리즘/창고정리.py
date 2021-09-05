n = int(input())
data = list(map(int,input().split()))
switch = int(input())

for _ in range(switch):
    small = big = data[0]
    big_idx = 0
    small_idx = 0

    for i in range(1,n):
        if data[i] <= small:
            small = data[i]
            small_idx = i
        elif data[i] >= big:
            big = data[i]
            big_idx = i
    data[big_idx] -= 1
    data[small_idx] += 1


print(max(data) - min(data))
