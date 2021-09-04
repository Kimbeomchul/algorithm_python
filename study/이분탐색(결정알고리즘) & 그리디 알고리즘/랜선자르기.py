n, m = map(int, input().split())
line = []
for _ in range(n):
    line.append(int(input()))

left = 1
right = max(line)
res = 0
while True:
    tot = 0
    middle = (left + right) // 2
    for i in line:
        tot += i // middle
    if tot >= m:
        res = middle
        left = middle + 1
    elif tot < m:
        right = middle - 1

    if left > right:
        break
print(res)
