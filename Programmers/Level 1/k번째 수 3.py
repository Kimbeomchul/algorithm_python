def solution(array, commands):
    answer = []

    for i in commands:
        temp = []
        a = i[1] - i[0]
        if a == 0:
            temp.append(array[i[0] - 1])
        else:
            for j in range(i[0] - 1, i[1]):
                temp.append(array[j])
        temp.sort()
        answer.append(temp[i[2] - 1])

    return answer