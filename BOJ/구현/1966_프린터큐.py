# 1966번 프린터 큐
from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    word = list(map(int, input().split()))

    q = deque((v, i) for i, v in enumerate(word))
    cnt = 0

    while q:
        n = q.popleft()

        if q and max(q)[0] > n[0]:
            q.append(n)
        else:
            cnt += 1
            if n[1] == m:
                break
    print(cnt)