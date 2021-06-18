#피보나치 함수 실버3 타임아웃
n = int(input())
data = []
temp0 = 0
temp1 = 0

def fibo(i):
    if i == 0:
        global temp0
        temp0 += 1
    elif i == 1:
        global temp1
        temp1 += 1
    else:
        return fibo(i-1) + fibo(i-2)

    return False


for i in range(n):
    data.append(int(input()))

for i in data:
    fibo(i)
    print(temp0,temp1)
    temp0 = 0
    temp1 = 0

