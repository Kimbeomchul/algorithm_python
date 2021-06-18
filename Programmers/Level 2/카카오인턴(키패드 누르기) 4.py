def check(current, picked):
    tolist = {1: [0, 0], 2: [0, 1], 3: [0, 2],
              4: [1, 0], 5: [1, 1], 6: [1, 2],
              7: [2, 0], 8: [2, 1], 9: [2, 2],
              '*': [3, 0], 0: [3, 1], '#': [3, 2]
              }

    cur = tolist.get(current)
    pic = tolist.get(picked)
    return abs(pic[0] - cur[0]) + abs(pic[1] - cur[1])


def solution(numbers, hand):
    answer = ''
    leftcurrent = '*'
    rightcurrent = '#'
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            leftcurrent = i

        elif i in [3, 6, 9]:
            answer += 'R'
            rightcurrent = i

        elif i in [2, 5, 8, 0]:
            dx = check(rightcurrent, i)
            dy = check(leftcurrent, i)
            if dx > dy:
                answer += 'L'
                leftcurrent = i
            elif dy > dx:
                answer += 'R'
                rightcurrent = i
            elif dx == dy:
                if hand == 'right':
                    answer += 'R'
                    rightcurrent = i
                else:
                    answer += 'L'
                    leftcurrent = i

    return answer