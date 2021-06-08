# 프로그래머스 카카오 개발자 겨울 인턴십 문제

def solution(board, moves):
    answer = 0
    stack = []
    lists = [[] for _ in range(len(board))]
    for i in board:
        for j in range(len(board)):
            lists[j].append(i[j])

    for i in moves:
        for j in lists[i - 1]:
            if j == 0:
                continue
            else:
                stack.append(j)
                lists[i - 1].remove(j)
                break
    temp = 0
    for i in range(len(stack)):
        for j in range(1, len(stack) - temp):
            if stack[j] != '/':
                if stack[j - 1] == stack[j]:
                    stack.pop(j - 1)
                    stack.pop(j - 1)
                    stack.append('/')
                    stack.append('/')
                    answer += 2
                    temp += 2

    return answer