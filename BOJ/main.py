# 연길이의 이상형

data = list(input())
list1 = ['E','S','T','J']
list2 = ['I','N','F','P']
res =[]
for i in range(len(data)):
    if data[i] is list1[i]:
        res.append(list2[i])
    else:
        res.append(list1[i])
print(''.join(res))
