#문자열 "aaabbbbbccccdaa"가 주어졌다고 가정하고 "a3b5c4d1a2"를 출력합니다.


data = "aaabbbbbccccdaa"
count = 1
answer = ""
for idx in range(1,len(data)):
    if data[idx] == data[idx-1]:
        count += 1
        continue
    answer += data[idx-1] + str(count)
    count = 1
if count != 1:
    answer += data[-1] + str(count)


print(answer)

