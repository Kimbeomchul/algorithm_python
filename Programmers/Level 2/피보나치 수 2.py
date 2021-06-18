import sys
from functools import lru_cache
sys.setrecursionlimit(1000001)

@lru_cache(maxsize=None)
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def solution(n):
    return int(fib(n) % 1234567)


#일반적인 재귀함수로는 타임아웃이뜬다
# lru_cache = 메모이제이션 사용
# DP도 가능