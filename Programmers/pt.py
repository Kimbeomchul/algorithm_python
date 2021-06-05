#프로그래머스 탐욕법 레벨 1 체육복

n = int(input())
lost = list(map(int,input().split()))
reserve = list(map(int,input().split()))

def solution(n, lost, reserve):
    answer = 0
    for i in reserve:
        if i-1 or i+1 in lost:
            answer += 1
    answer += (n-len(lost))
    if answer > n:
        answer = n
    return answer

print(solution(n,lost,reserve))

