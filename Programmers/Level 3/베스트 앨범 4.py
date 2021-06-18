# 해시

def solution(genres, plays):
    answer = []
    dics = {}
    for i in range(len(genres)):
        if genres[i] in dics:
            dics[genres[i]] += plays[i]
        else:
            dics[genres[i]] = plays[i]

    dics = sorted(dics.items(), key=lambda x: x[1], reverse=True)

    for i in range(len(dics)):
        temp = {}
        for idx, j in enumerate(genres):
            if dics[i][0] == j:
                temp[idx] = plays[idx]
        temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)
        for i in temp[:2]:
            answer.append(i[0])

    return answer
