def solution(progresses, speeds):
    answer = []
    day = []
    count = 0
    for idx, i in enumerate(progresses):
        while i < 100:
            i += speeds[idx]
            count += 1
        day.append(count)
        count = 0
    temp = day.copy()
    for idx, i in enumerate(day):
        if i == 0:
            count += 1
            continue
        elif i != 0 and idx != 0:
            answer.append(count)
            count = 0
        for j in range(len(day)):
            day[j] -= i
            if day[j] <= 0:
                day[j] = 0
        count += 1

    if count != 0:
        answer.append(count)

    return answer