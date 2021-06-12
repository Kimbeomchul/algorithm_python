def solution(d, budget):
    answer = 0
    d.sort()

    for i in range(len(d)):
        if budget < sum(d):
            d.pop()
        else:
            answer = len(d)
    return answer