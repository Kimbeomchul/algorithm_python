def solution(citations):
    answer = 0
    citations.sort()

    for idx, i in enumerate(citations):
        temp = citations[-(idx + 1)]
        if temp >= idx + 1:
            answer = idx + 1

    return answer