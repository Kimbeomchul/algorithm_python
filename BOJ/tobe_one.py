
# 두 입력값을 받아 1을 만들기 위한 문제
n,k = map(int,input().split())

count = 0


while n != 1:
    if (n % k == 0):
        n = n / k
        count += 1

    else:
        n = n-1
        count +=1

print(count)