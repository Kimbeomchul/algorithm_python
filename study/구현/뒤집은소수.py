n = int(input())
m = list(map(int,input().split()))
def reverse(x):
    temp = ''
    for _ in range(len(str(x))):
        temp += str(x % 10)
        x = int(x/10)
    return int(temp)

def isPrime(x):
    if x < 2:
        return 0
    for i in range(2,x):
        if x % i == 0:
            return 0
    return x


answer = []
for i in m:
    temp = isPrime(reverse(i))
    if temp != 0:
        answer.append(temp)
print(answer)
