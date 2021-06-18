import itertools


def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] += min(board[i - 1][j - 1], board[i][j - 1], board[i - 1][j])

    return max(itertools.chain(*board)) ** 2

# itertools.chain이 더빠르다 Sum(list,[]) 보다 !