n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
start = 0
end = len(data)-1

while True:
    middle = (start+end) // 2
    if start > end:
        print("EXIT")
        break

    if data[middle] == m:
        print(middle + 1)
        break
    elif data[middle] > m:
        end = middle - 1
    elif data[middle] < m:
        start = middle + 1
