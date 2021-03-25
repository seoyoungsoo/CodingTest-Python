# 4963번 섬의 개수
from collections import deque
import sys

input = sys.stdin.readline

dxy = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def BFS(j, k):
    q = deque()
    q.append((j, k))
    visited[j][k] = 1

    while q:
        x, y = q.popleft()
        for i in range(len(dxy)):  # 8면을 조사
            nx = x + dxy[i][0]
            ny = y + dxy[i][1]
            if 0 <= nx < h and 0 <= ny < w:
                if arrMap[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


while True:
    w, h = map(int, input().split())  # w가 열, h가 행
    if w == 0 and h == 0:
        break

    arrMap = [[0] * w for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0

    for i in range(h):
        arrMap[i] = list(map(int, input().split()))

    for j in range(h):
        for k in range(w):
            if arrMap[j][k] == 1 and visited[j][k] == 0:
                BFS(j, k)
                cnt += 1
    print(cnt)