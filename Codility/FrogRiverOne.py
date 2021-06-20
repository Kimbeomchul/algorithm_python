## 시간복잡도 O(n)

def solution(X, A):
    
    temp = [False] * X
    n = 0
    for idx, i in enumerate(A):
        if not temp[i-1]:
            temp[i-1] = True
            n+=1 
            if n == X: 
                return idx
    return - 1
