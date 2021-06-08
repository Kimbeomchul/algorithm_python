# 프로그래머스 카카오 블라인드 코딩테스트
def solution(N, stages):
    answer = []
    member = len(stages)
    fail = []

    for i in range(1, N + 1):
        if i in stages:
            a = stages.count(i)
            fail.append([a / member, i])
            member -= a
        else:
            fail.append([0, i])

    fail = sorted(fail, key=lambda x: [-x[0], x[1]])
    for i in fail:
        answer.append(i[1])

    return answer