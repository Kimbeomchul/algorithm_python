# [(1, 3), (5, 8), (4, 10), (20, 25)] 가 주어지면, [(1, 3), (4, 10), (20, 25)]

intervals2 = [(1, 3), (5, 8), (4, 10), (20, 25)]
intervals = [(1, 3), (5, 8), (4, 10), (20, 25), (22, 27)]
ans = []

intervals = sorted(intervals, key= lambda x: x[0])

for item in intervals:
    if ans and ans[-1][1] > item[1] or ans and ans[-1][1] > item[0]:
        ans[-1] = (ans[-1][0], max(ans[-1][1] , item[1]))
        continue
    ans.append(item)

print(ans)
