# 프로그래머스 카카오 개발자 겨울 인턴십 기출

def solution(stones, k):
    answer = 0
    while True:
        answer += 1
        for i in range(len(stones)):
            if stones[i] == 0:
                continue
            else:
                stones[i] -= 1
        count = 0
        for stone in stones:
            if stone == 0:
                count += 1
                if count == k:
                    return answer
            else:
                count = 0

# 정확성 100퍼 // 효용성 0 퍼 // 이분탐색써야함