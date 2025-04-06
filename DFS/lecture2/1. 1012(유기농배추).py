# 실버 3 유기농 배추  DFS- 같은 부류 찾기
# 백준 1012


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


T = int(input())

dirY = [-1,1,0,0]
dirX = [0,0,1,-1]

def dfs(y, x):
    global map_, visited
    visited[y][x] = True

    for i in range(4):
        newY = y + dirY[i] # 1
        newX = x + dirX[i] # 1
        # (0, 1) (2, 1) (1, 2) ( 1, 0)
        if map_[newY][newX] and not visited[newY][newX]:
             dfs(newY, newX)
n_list =[]
while T > 0:
    N, M, K = map(int,input().split())
    MAX = 50 +5

    map_ = [[False] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]

    for i in range(K):
        x, y = map(int,input().split())
        map_[y + 1][x + 1] = True
    
    order = 0
    for j in range(N + 1):
        for k in range(M + 1):
            if map_[j][k] and not visited[j][k]:
                dfs(j, k)
                order += 1
    n_list.append(order)
    T -= 1

for k in n_list:
    print(k)