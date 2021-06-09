from itertools import permutations


def check(n):
    array = [True for _ in range(10000001)]
    array[0] = False
    array[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if array[i]:
            for j in range(i + i, n + 1, i):
                array[j] = False

    return array


def solution(numbers):
    count = 0
    prime = check(10000000)
    arr = []
    for i in range(len(numbers)):
        a = set(list(permutations(numbers, i + 1)))

        for j in a:
            if int(''.join(j)) != 0 and int(''.join(j)) != 1 and int(''.join(j)) not in arr:
                arr.append(int(''.join(j)))
    for i in arr:
        if prime[i]:
            count += 1

    return count