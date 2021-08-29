n = int(input())
data = list(map(int,input().split()))
temp = []
answer = 0
def digit_sum(x):
    sum = 0
    for idx in range(len(str(x))):
        sum += x % 10
        x = int(x/10)
    return sum


for i in data:
    temp.append(digit_sum(i))
answer = data[temp.index(max(temp))]

print(answer)

