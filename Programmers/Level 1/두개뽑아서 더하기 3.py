from itertools import combinations


def solution(numbers):
    answer = []

    temp = list(combinations(numbers, 2))
    for i in temp:
        if sum(i) not in answer:
            answer.append(sum(i))
    answer.sort()

    return answer