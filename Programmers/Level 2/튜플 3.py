# 프로그래머스 카카오 개발자 인턴십 문제


# 2:57
def solution(s):
    answer = []
    temp = ''
    real = []
    real2 = []

    for i in range(len(s)):
        if s[i].isdigit():
            temp += s[i]
        if s[i] == ',':
            if s[i - 1].isdigit():
                temp += ','
        if s[i] == '}' and temp != '':
            real.append(temp)
            temp = ''
    for i in range(len(real)):
        a = real[i].split(',')
        real2.append(a)

    real2.sort(key=len)
    answer.append(int(real2[0][0]))

    for i in real2:
        for j in i:
            # print(i[j])
            if int(j) in answer:
                continue
            else:
                answer.append(int(j))
    return answer
