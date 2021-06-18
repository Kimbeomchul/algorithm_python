def solution(n):
    temp = ''

    while n > 0:
        n, m = divmod(n, 3)
        temp += str(m)

    return int(temp, 3)

# divmod(x,3) 나눠서 N , M 에 몫으로 저장
# 