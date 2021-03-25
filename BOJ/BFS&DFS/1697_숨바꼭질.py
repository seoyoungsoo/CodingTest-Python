# 1697번 숨바꼭질
from collections import deque
import sys

input = sys.stdin.readline


def BFS(idx):
    q = deque()
    q.append(idx)
    location[idx] = 0

    while q:
        n = q.popleft()
        time = [n - 1, n + 1, n * 2]

        for t in time:
            if 0 <= t <= 100000:
                if not location[t]:
                    location[t] = location[n] + 1

                    if location[K]:
                        return location[K]
                    q.append(t)


N, K = map(int, input().split())

location = [0 for _ in range(100001)]
if N == K:
    print(0)
else:
    print(BFS(N))
