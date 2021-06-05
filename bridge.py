# 백준 1010번 실버 5 다리놓기 문제
import math
num = input()
res =[]
for i in range(int(num)):
    n ,m = list(map(int,input().split()))

    res.append(math.factorial(m) // (math.factorial(m-n) * math.factorial(n)))

for a in range(int(num)):
    print(res[a])