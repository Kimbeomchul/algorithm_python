def solution(x, n):
    answer = []
    temp = 0
    for i in range(1,n+1):
        temp = x*i
        answer.append(temp)
        temp=0
    return answer