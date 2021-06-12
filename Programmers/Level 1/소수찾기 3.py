def prime(n):
    data = [True for i in range(n + 1)]
    data[0] = False
    data[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if data[i]:
            for j in range(i + i, n, i):
                data[j] = False

    return data.count(True)


def solution(n):
    return prime(n)