'''

문제
세계적인 도둑 상덕이는 보석점을 털기로 결심했다.

상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 상덕이는 가방을 K개 가지고 있고, 
각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.

상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)

다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)

다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)

모든 숫자는 양의 정수이다.

출력
첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력한다.

예제 입력 1 
2 1
5 10  # 보석 1 무게 가격
100 100 # 보석 2 무게 가격
11   # 가방이 담을 수 있는 최대 무게
예제 출력 1 
10
예제 입력 2 
3 2
1 65
5 23
2 99
10
2
예제 출력 2 
164

'''

import sys
input = sys.stdin.readline
from collections import deque
N, K = map(int,input().split())
n_list = [list(map(int,input().split())) for _ in range(N)]
w_list = [int(input()) for j in range(K)] # 10 , 2

n_list_dq = deque(sorted(n_list, key= lambda x: x[1], reverse= True))
w_list_dq = deque(sorted(w_list)) # 2, 10

# 2 99
# 1 65
# 5 23


tot = 0
while w_list_dq and n_list_dq:
        if n_list_dq[0][0] <= w_list_dq[0]:
            tot += n_list_dq[0][1]
            n_list_dq.popleft()
            w_list_dq.popleft()
        else:
            n_list_dq.popleft()

print(tot)



# 위 코드는 문제가 있음

'''
현재 코드의 근본적인 문제는 알고리즘 접근 방식에 있어요.
즉, 보석을 가격(가치) 순으로 내림차순 정렬한 후, 가장 작은 가방과 비교해서 맞으면 배정하고, 그렇지 않으면 보석을 버리는 방식은
**"가방에 맞는 보석"**을 제대로 고려하지 못합니다.

예를 들어, 아주 가치 높은 보석이 있지만 가장 작은 가방에는 들어가지 않을 경우, 그 보석이 그냥 버려지게 됩니다.
하지만 그 보석은 더 큰 가방에 들어갈 수 있으므로 활용되어야 합니다.

힌트:

가방을 용량 순(오름차순)으로 정렬하고,

각 가방에 대해 해당 가방에 들어갈 수 있는 보석들을 따로 모아
그 중 가치가 가장 높은 보석을 선택하는 방식(예: 최대 힙 활용)을 고려해 보세요.

이렇게 하면 각 가방마다 최적의 보석 선택이 가능해져서 전체 합이 최대가 될 수 있습니다.

'''


# gpt 힙으로 풀어야한다함
'''
import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
# 보석 정보를 (무게, 가격) 튜플 형태로 입력받음
jewels = [tuple(map(int, input().split())) for _ in range(N)]
# 각 가방의 최대 무게를 입력받음
bags = [int(input()) for _ in range(K)]

# 보석은 무게가 작은 순으로 정렬
jewels.sort(key=lambda x: x[0])
# 가방은 무게 용량이 작은 순으로 정렬
bags.sort()

answer = 0
max_heap = []
jewel_index = 0

# 각 가방에 대해 반복
for bag in bags:
    # 현재 가방에 담을 수 있는 보석들을 모두 최대 힙에 추가 (가격 기준, 음수값을 사용해 최대 힙 구현)
    while jewel_index < N and jewels[jewel_index][0] <= bag:
        heapq.heappush(max_heap, -jewels[jewel_index][1])
        jewel_index += 1
    # 가방에 담을 수 있는 보석이 있다면, 가장 가치가 높은 보석 선택
    if max_heap:
        answer += -heapq.heappop(max_heap)

print(answer)
''' 