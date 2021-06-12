def solution(n, words):
    answer = []
    stack = []
    idx = 0
    game = 0
    flag = 9
    for i in words:
        if not stack:
            stack.append(i)
            idx += 1
            game += 1
            continue

        idx += 1
        if idx == n + 1:
            idx = 1
            game += 1

        if len(i) == 1 or stack[-1][-1] != i[0] or i in stack:
            idx += 1
            flag = 1
            break
        stack.append(i)

    if flag == 9:
        return [0, 0]
    return [idx - 1, game]