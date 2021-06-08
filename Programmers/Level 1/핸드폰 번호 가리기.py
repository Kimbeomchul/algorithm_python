def solution(phone_number):
    answer = ''
    leng = len(phone_number)
    phone_number = phone_number[leng - 4:]
    answer += '*' * (leng - 4) + phone_number

    return answer