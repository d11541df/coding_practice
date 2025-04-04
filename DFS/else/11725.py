# DFS - 연결된 요소 찾기 유형
'''
트리의 부모 찾기

문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

예제 입력 1 
7
1 6
6 3
3 5
4 1
2 4
4 7
예제 출력 1 
4
6
1
3
1
4
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx):
    global graph, visited
    visited[idx] = True # 재방문 커트

    for i in range(1,N+1):
        if not visited and graph[idx][i]:
            dfs(i)


# 0. 입력 및 초기화
N = int(input())
MAX = 100000+ 10
graph = [[] for _ in range(N +1)]
visited = [False] * MAX
answer = [0]* MAX


# 1. 그래프 정보 받기기
for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for j in range(N+1):
    graph[j] = sorted(graph[j])

# 2. DFS 호출
for i in range(2,N+1):
    dfs(i)


# 3. 출력력



