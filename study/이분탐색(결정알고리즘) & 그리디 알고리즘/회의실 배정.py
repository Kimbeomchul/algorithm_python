n = int(input())
rooms = []

for _ in range(n):
    x, y = map(int,input().split())
    rooms.append([x,y])

rooms = sorted(rooms, key= lambda x: x[1])

temp = rooms[0][1]
counter = 1
for i in range(1,n):
    if temp <= rooms[i][0]:
        temp = rooms[i][1]
        counter += 1

print(counter)
