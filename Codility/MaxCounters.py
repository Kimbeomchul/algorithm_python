# MAX 사용으로인한 시간초과
# O(N+M) 도 88%라던데... 
# 아래코드는 68%...
def solution(N, A):
    data = [0] * N

    for i in A:
        if i == N+1:
            data = [max(data)] * N
            continue
        data[i-1] += 1


    return data
