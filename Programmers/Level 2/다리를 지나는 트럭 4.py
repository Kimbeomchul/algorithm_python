def solution(bridge_length, weight, truck_weights):
    time = 0
    stack = [0] * bridge_length

    while stack:
        stack.pop(0)
        time += 1
        if len(truck_weights) != 0:
            if sum(stack) + truck_weights[0] <= weight:
                stack.append(truck_weights.pop(0))
            else:
                stack.append(0)

    return time