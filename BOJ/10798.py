#백준 10798 세로읽기


data = []
ans = []

for _ in range(5):
    data.append(input())

max_len = 0
for i in data:
    if max_len < len(i):
        max_len = len(i)

for i in range(len(data)):
    if len(data[i]) < max_len:
        a = data[i].ljust(max_len,'.')
        data.remove(data[i])
        data.insert(i,a)

for i in range(max_len):
    for j in data:
        if j[i] == '.':
            continue
        ans.append(j[i])

print(''.join(ans))