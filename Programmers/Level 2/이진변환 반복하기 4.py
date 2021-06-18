def solution(s):
    count = 0
    count2 = 0
    while s != '1':
        count2 += s.count('0')
        s = s.replace('0', '')
        count += 1
        s = bin(len(s))[2:]

    return [count, count2]