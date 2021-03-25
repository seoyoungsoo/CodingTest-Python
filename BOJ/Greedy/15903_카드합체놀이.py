# 15903번 카드 합체 놀이

import heapq as hq

N, M = map(int, input().split())
cards = list(map(int, input().split()))
hq.heapify(cards)

for i in range(M):
    num = hq.heappop(cards) + hq.heappop(cards)
    hq.heappush(cards, num)
    hq.heappush(cards, num)
print(sum(cards))