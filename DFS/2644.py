import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx, count):
    global graph, visited, end, answer
    visited[idx] = True # 재방문 방지
    if idx == end:
        answer = count
        return

    for i in range(1, N + 1):
        if not visited[i] and graph[idx][i]: # 방문한 적이 없고 graph의 idx와 i가 인접한다면면
            dfs(i, count + 1)


# 0. 입력 및 초기화
N = int(input())
start = int(input())
end = int(input())
M = int(input())
graph = [[False] * (N + 1) for _ in range(N+1)]
visited = [False] * (N + 1)
answer = -1


for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

for j in range(N+1):
    graph[j] = sorted(graph[j])

dfs(start, 0)