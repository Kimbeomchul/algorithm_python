def solution(N):
    N = (bin(N)[2:])
    if N.count('1') == 1 or '0' not in N:
        return 0
    else:
        N = N.split('1')
    N.sort(key=len)
    return int(len(N[-1]))