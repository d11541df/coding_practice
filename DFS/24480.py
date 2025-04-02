import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx):
    global visited, graph, result, order
    visited[idx] = True
    result[idx] = order
    order += 1

    for i in graph[idx]:
        if not visited[i]:
            dfs(i)



N, M, R = map(int, input().split())
Max = 100000 + 10
graph = [[] for _ in range(N + 1)]
visited = [False] * Max
result = [0] * Max
order = 1

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1, N + 1):
    graph[i] = sorted(graph[i], reverse= True)



dfs(R)

for i in range(1, N+1):
    print(result[i])