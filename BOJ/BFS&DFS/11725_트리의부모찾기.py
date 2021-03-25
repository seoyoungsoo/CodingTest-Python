# 11725번 트리의 부모 찾기
# 코드참조: https://velog.io/@bye9/백준파이썬-11725-트리의-부모-찾기
from collections import deque
import sys

input = sys.stdin.readline


def BFS(i):
    q = deque()
    q.append(i)

    while q:
        n = q.popleft()
        for num in graph[n]:
            if parents[n - 1] != num:
                parents[num - 1] = n
                q.append(num)


N = int(input())
graph = {i: [] for i in range(1, N + 1)}
parents = [0] * N

for i in range(N - 1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

BFS(1)

for node in parents[1:]:
    print(node)