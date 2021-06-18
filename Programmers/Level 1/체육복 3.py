def solution(n, lost, reserve):
    r = [i for i in reserve if i not in lost]
    l = [j for j in lost if j not in reserve]

    for i in r:
        if i - 1 in l:
            l.remove(i - 1)
        elif i + 1 in l:
            l.remove(i + 1)

    return n - len(l)