def solution(n):
    answer = list(str(n)[::-1])
    for idx,i in enumerate(answer):
        answer[idx] = int(i)
    return answer