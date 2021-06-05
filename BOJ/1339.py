# 백준 1339 단어수학

n = int(input())
data =[]
dicts = {}
for inputs in range(n):
    data.append(input())

for i in data:
    res = 0
    for j in i:
        if j not in dicts:
            dicts[j] = 10 ** (len(i)-res-1)
        elif j in dicts:
            dicts[j] += 10 ** (len(i) - res - 1)

        res += 1

dic_list = list(dicts.values())
dic_list.sort(reverse=True)
cnt = 9
ans = 0
for count in range(len(dic_list)):
    ans += dic_list[count] * (cnt-count)
print(ans)
