# 2644번 촌수계산
# 코드 참조 // https://gingerkang.tistory.com/11

from collections import deque as dq


def family(p1):
    visited[p1] = True
    q = dq([p1])
    count = 0

    while q:
        count += 1
        for _ in range(len(q)):
            n = q.popleft()
            if n == p2:
                return count - 1
            for num in graph[n]:
                if visited[num] == False:
                    visited[num] = True
                    q.append(num)
    return -1


n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
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

visited = [False] * (n+1)
print(family(p1))