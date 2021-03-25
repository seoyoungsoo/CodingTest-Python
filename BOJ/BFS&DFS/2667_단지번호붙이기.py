# 2667번 단지번호붙이기
from collections import deque
import sys

input = sys.stdin.readline


def BFS(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j], cnt = 1, 1

    while q:
        x, y = q.popleft()
        for i in range(len(dxy)):
            dx = x + dxy[i][0]
            dy = y + dxy[i][1]
            if 0 <= dx < N and 0 <= dy < N:
                if Map[dx][dy] == 1 and visited[dx][dy] == 0:
                    visited[dx][dy] = 1
                    cnt += 1
                    q.append([dx, dy])
    arr.append(cnt)

N = int(input())
Map = [list(map(int, input()[:-1])) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

arr = list()
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(N):
    for j in range(N):
        if Map[i][j] == 1 and visited[i][j] == 0:
            BFS(i, j)

arr.sort()
print(len(arr))
for i in arr:
    print(i)