def solution(s):
    s = s.split(' ')

    for idx, i in enumerate(s):
        if i == '':
            continue
        i = i[0].upper() + i[1:].lower()
        s[idx] = i
    return ' '.join(s)