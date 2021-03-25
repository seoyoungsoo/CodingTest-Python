# 1012번 유기농 배추
from collections import deque
import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        n = q.popleft()
        for i in range(4):  # 사방면 확인
            ny = n[0] + dy[i]
            nx = n[1] + dx[i]
            if 0 <= nx < M and 0 <= ny < N:
                if arr[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny,nx))


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                BFS(i, j)
                cnt += 1
    print(cnt)