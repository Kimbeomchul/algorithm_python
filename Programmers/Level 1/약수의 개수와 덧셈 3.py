def prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


def solution(left, right):
    ans = 0
    for i in range(left, right + 1):
        temp = prime(i)
        if temp % 2 == 0:
            ans += i
        elif temp % 2 != 0:
            ans -= i

    return ans