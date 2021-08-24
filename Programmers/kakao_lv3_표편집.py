import heapq
def solution(n, k, cmd):
    left_idx = []
    right_idx = []
    
    for idx in range(k):
        heapq.heappush(left_idx , -idx)
    for idx in range(k,n):
        heapq.heappush(right_idx, idx)
    
    backup = []
    for command in cmd:
        if len(command)>1:
            slt = int(command.split()[-1])
            if command[0] == "D":
                for _ in range(slt):
                    if right_idx:
                        heapq.heappush(left_idx , -heapq.heappop(right_idx))
            elif command[0] == "U":
                for _ in range(slt):
                    if left_idx:
                        heapq.heappush(right_idx , -heapq.heappop(left_idx))
                    
        elif command[0] == "C":
            backup.append(heapq.heappop(right_idx))
            if not right_idx:
                heapq.heappush(right_idx, -heapq.heappop(left_idx))
            

        elif command[0] == "Z":
            temp = backup.pop()
            if right_idx[0] > temp:
                heapq.heappush(left_idx , -temp)
            else:
                heapq.heappush(right_idx , temp)
    ans = []
    while right_idx and left_idx:
        ans.append(-heapq.heappop(left_idx))
        ans.append(heapq.heappop(right_idx))
    ans.sort()
    print(ans)
    answer = ["O" if i in ans else "X" for i in range(n)]
    print(answer)
    return ''.join(answer)
