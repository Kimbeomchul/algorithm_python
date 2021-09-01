n = int(input())
apple_tree = []

for _ in range(n):
    apple_tree.append(list(map(int,input().split())))


apples = 0
for i in range(n//2):
    apples += sum(apple_tree[i][n//2-i:n//2+1+i])
    apples += sum(apple_tree[-(i+1)][n//2-i:n//2+1+i])
apples += sum(apple_tree[n//2])
print(apples)
