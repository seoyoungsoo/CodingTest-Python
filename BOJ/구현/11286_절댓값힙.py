# 11286 절댓값 힙
# 코드참조: https://huidea.tistory.com/40

import heapq
import sys
input = sys.stdin.readline

n = int(input())
hq = []
for i in range(n):
    num = int(input())

    if num:
        heapq.heappush(hq, (abs(num), num))
    else:
        try:
            print(heapq.heappop(hq)[1])
        except IndexError:
            print(0)