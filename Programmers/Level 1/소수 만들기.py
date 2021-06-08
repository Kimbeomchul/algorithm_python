from itertools import combinations
import math


def isPrime(n):
    k = math.sqrt(n)
    if n < 2:
        return False

    for i in range(2, int(k) + 1):
        if n % i == 0:
            return False
    return True


def solution(nums):
    count = 0
    data = list(combinations(nums, 3))

    for i in data:
        added = sum(i)
        if isPrime(added):
            count += 1

    return count