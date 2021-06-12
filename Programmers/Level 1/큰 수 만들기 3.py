k = int(input())
number = input()
m = len(number) - k
for i in range(k+1):
    for j in range(i,i+m):
        print(number[j])
    print('--')
array= [1,2,3]
