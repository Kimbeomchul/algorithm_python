# 백준 1978번 소수찾기

n = int(input())
data = list(map(int, input().split()))
count = 0

def define_prime(num):
    if num == 1:
        return False

    for x in range(2, num):
        if num % x == 0:
            return False
    return True


for i in data:
    dt = define_prime(i)
    if dt is True:
        count += 1
print(count)