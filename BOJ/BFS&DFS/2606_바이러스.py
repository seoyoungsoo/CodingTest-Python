# 2606번 바이러스

from collections import deque


def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                tmp = list(set(graph[n]) - set(visited))
                queue += tmp
    print(len(visited)-1)


def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                tmp = list(set(graph[n]) - set(visited))
                stack += tmp
    print(len(visited)-1)


com = int(input())
connect = int(input())
graph = dict()

for i in range(connect):
    n1, n2 = map(int, input().split())
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

BFS(graph, 1)
DFS(graph, 1)