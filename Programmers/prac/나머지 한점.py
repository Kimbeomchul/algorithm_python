def solution(v):
    answer = []

    for a, b, c in zip(v[0], v[1], v[2]):
        if a == b:
            answer.append(c)
        elif b == c:
            answer.append(a)
        elif a == c:
            answer.append(b)
    return answer