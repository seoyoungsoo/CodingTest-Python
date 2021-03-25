# 11724번 연결 요소의 개수
from collections import deque
import sys

input = sys.stdin.readline

# 코드는 정상적으로 돌아가지만 효율성에서 걸림
'''def BFS(i):
    q = deque()
    q.append(i)

    while q:
        n = q.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                tmp = list(set(graph[n]) - set(visited))
                q += tmp


N, M = map(int, input().split())
graph, visited = dict(), list()
cnt = 0

for i in range(M):
    u, v = map(int, input().split())

    if u not in graph:
        graph[u] = [v]
    elif v not in graph[u]:
        graph[u].append(v)
    if v not in graph:
        graph[v] = [u]
    elif u not in graph[v]:
        graph[v].append(u)

for i in range(1, N + 1):
    if i not in visited:
        BFS(i)
        cnt += 1
print(cnt)'''


# 새로운 풀이
def BFS(i):
    q = deque()
    q.append(i)

    while q:
        n = q.popleft()
        for i in graph[n]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

cnt = 0
for i in range(1, N + 1):
    if visited[i] == 0:
        BFS(i)
        cnt += 1
print(cnt)
