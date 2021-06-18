def solution(answers):
    answer = []
    player1 = [1, 2, 3, 4, 5]
    player2 = [2, 1, 2, 3, 2, 4, 2, 5]
    player3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    p1 = 0
    p2 = 0
    p3 = 0
    i = 0
    a = 0
    b = 0
    c = 0
    while i != len(answers):
        if a >= len(player1):
            a = 0
        if b >= len(player2):
            b = 0
        if c >= len(player3):
            c = 0

        if answers[i] == player1[a]:
            p1 += 1
        if answers[i] == player2[b]:
            p2 += 1
        if answers[i] == player3[c]:
            p3 += 1

        i += 1
        a += 1
        b += 1
        c += 1

    temp = max(p1, p2, p3)
    if temp == p1:
        answer.append(1)
    if temp == p2:
        answer.append(2)
    if temp == p3:
        answer.append(3)

    answer.sort()

    return answer
