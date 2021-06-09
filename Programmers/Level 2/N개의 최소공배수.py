from math import gcd


def solution(arr):
    answer = 0
    temp = 0
    for i in range(1, len(arr)):
        temp = (arr[i - 1] * arr[i]) // gcd(arr[i - 1], arr[i])
        arr[i] = temp

    return temp