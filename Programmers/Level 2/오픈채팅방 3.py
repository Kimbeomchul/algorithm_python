#프로그래머스 카카오 문제

def solution(record):
    answer = []
    data = []
    dics = {}
    uuid = []
    for i in record:
        a = i.split(' ')
        data.append(a)

    for i in data:
        if i[0] == 'Change' or i[0] == 'Enter':
            dics[i[1]] = i[2]

    for i in data:
        if i[0] == 'Enter':
            temp = dics.get(i[1])
            temp = temp + '님이 들어왔습니다.'
            answer.append(temp)
        elif i[0] == 'Leave':
            temp = dics.get(i[1])
            temp = temp + '님이 나갔습니다.'
            answer.append(temp)
    return answer