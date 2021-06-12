#  백준 10162번 전자레인지

n = int(input())
sec = [300,60,10]
result =[0 for x in range(len(sec))]
temp = ''
if n % 10 != 0:
    print(-1)
    exit()

for i in range(len(sec)):
    result[i] = n // sec[i]
    n = n % sec[i]
    temp += str(result[i]) + ' '
print(temp)