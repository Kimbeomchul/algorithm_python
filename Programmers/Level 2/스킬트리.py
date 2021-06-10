def solution(skill, skill_trees):
    answer = 0
    temp = ''
    idx = []

    for i in skill_trees:
        for j in i:
            if j in skill:
                temp += j
            else:
                continue
        idx.append(temp)
        temp = ''

    for i in idx:
        for j in range(len(i)):
            if skill[j] == i[j]:
                continue
            else:
                answer -= 1
                break
        answer += 1

    return answer