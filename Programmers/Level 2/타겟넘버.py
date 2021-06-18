from itertools import product


def solution(numbers, target):
    data = [[i, -i] for i in numbers]

    res = list(map(sum, product(*data)))

    return res.count(target)