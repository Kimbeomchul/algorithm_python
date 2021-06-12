def solution(n):
    answer = 0
    temp = int(n**0.5)
    if temp * temp == n:
        answer = (temp+1)**2
    else:
        answer = -1
    return answer