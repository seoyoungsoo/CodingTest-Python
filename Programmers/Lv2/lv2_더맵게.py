# 더 맵게

# 나의 풀이
# Heap을 사용한 풀이
import heapq


def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)

    while scoville:
        if scoville[0] < K and len(scoville) > 1:
            tmp1 = heapq.heappop(scoville)
            tmp2 = heapq.heappop(scoville)
            heapq.heappush(scoville, tmp1 + (tmp2 * 2))
            cnt += 1
        else:
            break

    if scoville[0] < K:
        return -1
    else:
        return cnt


# testcase1
scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))