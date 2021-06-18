# 더하기 or 곱하기

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num is 1 or num is 0 or result is 0:
        result += num
    else:
        result *= num
print(result)
