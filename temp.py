input = [(1,3), (5,8), (4,10), (20,25)]

input = sorted(input, key= lambda x: x[0])
ans = []
temp = 99999 

for i in range(1,len(input)):
    if temp == (i-1):
        continue
    if input[i-1][1] >= input[i][1]:
        temp = i
    ans.append((input[i-1][0], input[i-1][1]))
ans.append((input[-1][0], input[-1][1]))
    
print(ans)
