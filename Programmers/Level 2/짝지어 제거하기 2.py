def solution(s):
    answer = -1
    data = []
    for i in s:
        if i not in data:
            data.append(i)
        else:
            temp = data.pop()
            if temp != i:
                data.append(temp)
                data.append(i)

    if len(data) == 0:
        answer = 1
    else:
        answer = 0
    return answer