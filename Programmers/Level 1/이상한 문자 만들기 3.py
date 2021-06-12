def solution(s):
    s = s.split(' ')
    print(s)
    ans = ''
    for i in s:
        for idx,j in enumerate(i):
            if idx % 2 == 0:
                ans += i[idx].upper()
            else:
                ans += i[idx].lower()
        ans += ' '
    return ans[:-1]