# 효용성테스트 실패

def solution(participant, completion):
    for i in completion:
        participant.remove(i)

    return participant[0]


#remove쓰면 거의다 타임아웃...

# 성공
import collections


def solution(participant, completion):
    count = collections.Counter(participant)
    ans = ''
    for i in completion:
        count[i] -= 1

    for i, j in count.items():
        if j == 1:
            ans = i
            break

    return ans


