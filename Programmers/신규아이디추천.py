# 프로그래머스 카카오 블라인드 채용 코딩테스트
# 문자열을 자르기 위해 re.sub 사용 

import re

def solution(new_id):
    answer = re.sub(r"[^a-z0-9-_.]", "", new_id.lower())

    while True:
        if '..' in answer:
            answer = answer.replace('..', '.')
        else:
            break
    if answer != '':
        if answer[0] == '.':
            answer = answer[1:]
            if answer == '':
                answer += 'a'

        if answer[-1] == '.':
            answer = answer[:-1]
            if answer == '':
                answer += 'a'
    else:
        answer += 'a'

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    elif len(answer) <= 2:
        temp = answer[-1]
        while len(answer) != 3:
            answer += temp

    return answer