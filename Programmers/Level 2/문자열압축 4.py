def solution(s):
    rng = (len(s) // 2) + 1
    ans = 99999999
    for i in range(1, rng):
        temp = ''
        count = 1
        cut = s[:i]

        for j in range(i, len(s) + i, i):
            if s[j:i + j] == cut:
                count += 1
            else:
                if count != 1:
                    temp = temp + str(count) + cut

                else:
                    temp += cut

                count = 1
                cut = s[j:j + i]

        ans = min(ans, len(temp))

    return min(ans, len(s))