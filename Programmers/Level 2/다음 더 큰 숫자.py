
def solution(n):
    answer = 0
    counter = bin(n)[2:].count('1')

    while True:
        n += 1
        if bin(n)[2:].count('1') == counter:
            break

    return n