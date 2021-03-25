# 5567번 결혼식
from collections import deque
import sys

input = sys.stdin.readline


def BFS(i):
    q = deque([i])
    visited = [i]

    for idx in graph[i]:
        q.append(idx)

    while q:
        n = q.popleft()
        for num in graph[n]:
            if num not in visited:
                visited.append(num)
    return len(visited)-1


n = int(input())
graph = {x: [] for x in range(1, n+1)}
m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(BFS(1))
