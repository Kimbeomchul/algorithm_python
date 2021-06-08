def solution(n):
    answer = ''
    a ='수박'
    for i in range(n):
        answer += a[i%len(a)]
    return answer