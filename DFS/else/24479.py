import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx):
    global graph, visited, answer, order
    visited[idx] = True
    answer[idx] = order
    order += 1

    for i in graph[idx]:
        if not visited[i]:
            dfs(i)



N, M, R = map(int,input().split())
MAX = 100000 + 10

graph = [[] for _ in range(N + 1)]
visited = [False] * MAX
answer = [0] * MAX
order = 1

#1. graph 정보 받기
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
#2. 오름차순 정렬
for i in range(1, N+1):
    graph[i] = sorted(graph[i])

# DFS 호출
dfs(R)



# 4. 출력
for i in range(1, N+1):
    print(answer[i])


