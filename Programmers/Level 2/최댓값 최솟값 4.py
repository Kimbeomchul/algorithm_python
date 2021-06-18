def solution(s):
    answer = ''
    data = sorted(list(map(int,s.split(' '))))
    answer += str(data[0]) +' '+ str(data[-1])
    return answer