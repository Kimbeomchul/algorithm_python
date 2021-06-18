def solution(n):
    res = []
    for i in str(n):
        res.append(i)

    return int(''.join(sorted(res, reverse=True)))