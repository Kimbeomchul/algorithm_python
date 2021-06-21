def solution(A):
    
    A.sort()

    for idx,i in enumerate(A):
        if idx+1 != i:
            return 0

    return 1
