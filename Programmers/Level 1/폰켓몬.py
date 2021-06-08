# 프로그래머스
# itertools 의 combinations사용시 시간초과
#

import collections
def solution(nums):
    answer = 0

    temp = int(len(nums) / 2)
    a = collections.Counter(nums)
    if temp <= len(a.items()):
        answer = temp
    elif temp > len(a.items()):
        answer = len(a.items())

    return answer