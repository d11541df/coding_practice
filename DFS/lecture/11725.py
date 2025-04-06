'''
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	103491	47420	33203	43.404%
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
예제 입력 2 
12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
예제 출력 2 
1
1
2
3
3
4
4
5
5
6
6
'''

import sys
import time


sys.setrecursionlimit(10**6)
input = sys.stdin.readline
start_time = time.time()

def dfs(idx):
    global graph, visited, answer
    visited[idx] = True

    for i in graph[idx]:
        if not visited[i]:
            answer[i] = idx
            dfs(i)




N = int(input())
MAX = 100000 + 10
graph = [[] for _ in range(N+1)]
visited = [False] * MAX
answer = [0] * MAX

for i in range(N-1):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)


dfs(1)


for i in range(2, N+1):
    print(answer[i])

end_time = time.time()
print(f"전체 실행 시간: {end_time - start_time} 초")