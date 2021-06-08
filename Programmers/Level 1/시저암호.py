def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
            continue
        if 97 <= ord(i) <= 122:
            temp = ord(i) + n
            if temp > 122:
                temp -= 26
            answer += chr(temp)

        else:
            temp = ord(i) + n
            if temp > 90:
                temp -= 26
            answer += chr(temp)

    return answer