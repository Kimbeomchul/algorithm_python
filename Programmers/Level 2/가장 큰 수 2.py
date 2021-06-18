def solution(numbers):
    data = list(map(str,numbers))
    data.sort(key= lambda x:x*3, reverse=True) # 문자열 곱하기
    return str(int(''.join(data)))