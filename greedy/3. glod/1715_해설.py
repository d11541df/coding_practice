import sys
import heapq

input = sys.stdin.readline
N = int(input())

heap = []
for _ in range(N):
    n = int(input())
    heapq.heappush(heap, n)

# 카드 묶음이 하나만 있다면 합칠 필요가 없으므로 비용은 0
if N == 1:
    print(0)
else:
    cost = 0
    # 최소 힙에서 두 개씩 꺼내서 합친 후, 다시 힙에 넣기
    while len(heap) > 1:
        x = heapq.heappop(heap)  # 가장 작은 카드 묶음
        y = heapq.heappop(heap)  # 두 번째로 작은 카드 묶음
        sum_xy = x + y          # 두 묶음을 합친 비용
        cost += sum_xy          # 누적 비용에 더함
        heapq.heappush(heap, sum_xy)  # 합친 묶음을 다시 힙에 넣음

    print(cost)
