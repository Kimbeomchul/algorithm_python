## Time Complexity
## Detected time complexity:
## O(N) or O(N * log(N))

# 첫번째 트라이 - 예외처리로인한 런타임에러 

def solution(A):
    return sum(range(len(A)+2)) - sum(A)



## 2번쨰 트라이 

def solution(A):
    if not A:
        return 1
        
    if min(A) == 0:
        return 1
    
    return sum(range(len(A)+2)) - sum(A)
