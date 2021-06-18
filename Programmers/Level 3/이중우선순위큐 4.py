import heapq as hq


def solution(operations):
    answer = []

    heap = []

    for i in operations:
        temp = i.split(' ')
        if temp[0] == 'I':
            hq.heappush(heap, int(temp[1]))
        elif temp[0] == 'D':
            try:
                if int(temp[1]) == 1:
                    heap.remove(max(heap))
                else:
                    hq.heappop(heap)
            except:
                continue

    if not heap:
        return [0, 0]
    else:
        heap = list(map(int, heap))
        answer.append(max(heap))
        answer.append(min(heap))
    return answer