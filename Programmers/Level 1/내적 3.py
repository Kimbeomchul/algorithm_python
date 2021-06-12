def solution(a, b):
    c = len(a)

    ans = 0
    for i in range(c):
        ans += a[i] * b[i]

    return ans
