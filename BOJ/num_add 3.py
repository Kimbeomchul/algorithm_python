# 더하기 사이클 백준 1110번 브론즈 1
# 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.

n = input()
count = 0
temp = list(n)
ans = ''
temp = 0
first = n

if int(n) < 10:
    n = '0' + str(n)
    first = n
while True:
    if int(n) == 0:
        count += 1
        break
    if first == ans:
        break
    temp = int(n[0]) + int(n[1])
    if temp >= 10:
        temp = temp % 10
    ans = n[1] + str(temp)
    n = ans
    count += 1

print(count)