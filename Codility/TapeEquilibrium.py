# 첫트라이 - O(n * n) 60%

def solution(A):
    comp = 100001
    for i in range(1,len(A)):
        temp = abs(sum(A[:i]) - sum(A[i:]))
        if comp > temp:
            comp = temp
    return comp

 # 두번째 - O(n) 100%

def solution(A):
    comp = 100001
    s = sum(A)
    
    for i in range(len(A)-1):
        s -= (A[i]*2)
        if comp > abs(s):
            comp = abs(s)
    return comp
