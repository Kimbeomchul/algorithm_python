def solution(A, K):
    for i in range(1,K+1):
        temp = A.pop(-1)
        A.insert(0,temp)

    return A
