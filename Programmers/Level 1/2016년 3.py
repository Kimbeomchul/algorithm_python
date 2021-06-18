
def solution(a, b):
    answer = ''
    days = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    temp = 0

    for i in range(1, a):
        temp += days.get(i)

    temp += b
    for i in range(temp):
        answer = day[i % len(day)]

    return answer