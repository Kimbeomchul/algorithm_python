n , m = list(map(int,input().split()))
data = list(map(int,input().split()))
ans = 0
left = 0
right = 1

temp = data[0]


while left < n:
    if temp < m:
        if right < n:
            temp += data[right]
            right += 1
        else:
            break
    elif temp == m:
        ans += 1
        temp -= data[left]
        left += 1

    else:
        temp -= data[left]
        left += 1

print(ans)
