
## Detected time complexity:
## O(N) or O(N*log(N))

from collections import Counter
def solution(A):

    temp = Counter(A)
    for i in temp:
        if temp.get(i) % 2 != 0:
            return i
    return 0

