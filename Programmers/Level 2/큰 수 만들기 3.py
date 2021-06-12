def solution(number, k):
    stack = [number[0]]

    for i in number[1:]:

        while len(stack) > 0 and stack[-1] < i:
            if k == 0:
                break
            k -= 1
            stack.pop()

        stack.append(i)

    if k != 0:
        while k != 0:
            stack.pop(-1)
            k -= 1

    return str(''.join(stack))