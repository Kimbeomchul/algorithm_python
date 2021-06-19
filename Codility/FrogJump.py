## Detected time complexity:
## O(1)

# Time Complexity Question


def solution(X, Y, D):
    temp = Y-X
    ans = 0
    if temp % D != 0:
        ans = int(temp/D) +1
    else:
        ans = int(temp/D)
    

    return ans
