n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
counter = 0
idx = 0
while len(data) != 0:

    if data[idx] + data[-1] <= m:
        data.pop(idx)
        try:
            data.pop(-1)
        except:
            counter += 1
            break
        counter += 1
        continue
    elif data[idx] <= m:
        data.pop(idx)
        counter += 1
        continue
    idx += 1
print(counter)
