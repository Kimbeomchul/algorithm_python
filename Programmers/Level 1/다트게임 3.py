#카카오 블라인드 채용


def solution(dartResult):
    answer = 0
    data = []
    temp = 0
    dartResult = dartResult.replace('10', 'z')
    for i in range(len(dartResult)):

        if dartResult[i].isdigit() or dartResult[i] == 'z':
            if temp != 0:
                data.append(temp)
                temp = 0
            if dartResult[i] == 'z':
                temp += 10
            else:
                temp += int(dartResult[i])

        if dartResult[i] == 'S':
            temp = temp ** 1
        elif dartResult[i] == 'D':
            temp = temp ** 2
        elif dartResult[i] == 'T':
            temp = temp ** 3

        if dartResult[i] == '*':
            if len(data) != 0:
                data[-1] = data[-1] * 2
            temp *= 2

        if dartResult[i] == '#':
            temp *= -1

    if temp != 0:
        data.append(temp)

    return sum(data)