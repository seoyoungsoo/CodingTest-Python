# 1325번 효율적인 해킹
from collections import deque
import sys

input = sys.stdin.readline


def BFS(i):
    q = deque([i])
    visited = [0 for _ in range(N+1)]
    visited[i] = 1
    cnt = 1

    while q:
        n = q.popleft()
        for k in graph[n]:
            if visited[k] == 0:
                visited[k] = 1
                cnt += 1
                q.append(k)
    return cnt


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

hacking = []
maxN = 0
for i in range(1, N + 1):
    if graph[i]:
        tmp = BFS(i)
        if maxN == tmp:
            hacking.append(i)
        elif maxN < tmp:
            maxN = tmp
            hacking = [i]

print(*hacking)