# 1260번 DFS와 BFS


def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                tmp = list(set(graph[n]) - set(visited))
                tmp.sort(reverse=True)
                stack += tmp
    print(' '.join(str(i) for i in visited))


def BFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop(0)
        if n not in visited:
            visited.append(n)
            if n in graph:
                tmp = list(set(graph[n]) - set(visited))
                tmp.sort()
                stack += tmp
    print(' '.join(str(i) for i in visited))


n, m, v = map(int, input().split())
graph = dict()

for i in range(m):
    n1, n2 = map(int, input().split())
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

DFS(graph, v)
BFS(graph, v)