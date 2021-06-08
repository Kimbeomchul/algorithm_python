def solution(lottos, win_nums):
    answer = []
    dics = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}
    count = 0
    q = 0
    for i in lottos:
        if i in win_nums:
            count += 1
            continue
        if i == 0:
            q += 1

    if q == 0:
        if count <= 1:
            a = 6
        else:
            a = dics.get(count)
        answer = [a, a]
        return answer
    else:
        if count <= 1:
            a = 6
        else:
            a = dics.get(count)
        b = dics.get(count + q)
        answer.append(b)
        answer.append(a)
        return answer

    return answer