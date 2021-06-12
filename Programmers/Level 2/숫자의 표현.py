def solution(n):
    ans = 0
    sq = int(n / 2) + 1
    temp = 0
    for j in range(1, sq):
        for i in range(j, sq + 1):
            temp += i
            if temp == n:
                ans += 1
                break
            elif temp > n:
                break
        temp = 0

    return ans + 1