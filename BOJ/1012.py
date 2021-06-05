#백준 1012 유기농배추
import sys
sys.setrecursionlimit(10000)
n = int(input())

def DFS(i,j):

    if i <= -1 or i >= b or j <= -1 or j >= a:
        return False
    if checked[i][j] == 1:
        checked[i][j] = 0
        DFS(i-1, j)
        DFS(i, j-1)
        DFS(i+1, j)
        DFS(i, j+1)
        return True
    return False


for _ in range(n):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    input_data = []
    baechu = []
    a , b , c = map(int,input().split())
    checked = [[0 for _ in range(a)] for _ in range(b)]

    count = 0
    for x in range(c):
        temp = list(map(int,input().split()))
        baechu.append((temp[1],temp[0]))
        checked[temp[1]][temp[0]] = 1

    for i in range(b):
        for j in range(a):
            if DFS(i,j):
                count += 1


    print(count)