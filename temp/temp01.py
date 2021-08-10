intervals2 = [(1, 3), (5, 8), (4, 10), (20, 25)]
intervals = [(1, 3), (5, 8), (4, 10), (20, 25), (22, 27)]
data = []
 
intervals = sorted(intervals, key = lambda x: x[0])
 
for item in intervals:
    if data and data[-1][1] >= item[1] or data and data[-1][1] >= item[0]:
        data[-1] = (data[-1][0] , max(item[1] , data[-1][1]))
    else:
        data.append(item)
    
    
print(data)
 
 # 1. ans [(1, 3), (4, 10), (20, 27)]
 # 2. ans [(1, 3), (4, 10), (20, 25)]
 
