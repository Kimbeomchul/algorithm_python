def solution(A):
    checker = [False] * 100001

    for i in A:
        if i > 0:
            checker[i - 1] = True

    for i in range(100001):
        if not checker[i]:
            return i + 1