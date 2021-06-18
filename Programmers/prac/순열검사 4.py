def solution(arr):
    answer = True
    arr.sort()
    for idx, i in enumerate(arr):
        if idx + 1 != i:
            return False

    return answer