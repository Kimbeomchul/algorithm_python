def solution(priorities, location):
    alpha =[i for i in range(101)]
    temp = priorities.copy()
    temp.sort(reverse=True)
    for i in range(len(priorities)):
        priorities[i] = [priorities[i],alpha[i]]

    key = priorities[location][1]

    count = 0
    while True:

        if priorities[0][0] == temp[0]:
            if priorities[0][1] == key:
                count += 1
                break
            else:
                count += 1
                temp.pop(0)
                priorities.pop(0)
        else:
            a = priorities.pop(0)
            priorities.append(a)


    return count