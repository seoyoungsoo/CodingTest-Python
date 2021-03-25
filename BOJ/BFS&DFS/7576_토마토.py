# 7576번 토마토
# 코드참조: https://it-garden.tistory.com/174
from collections import deque
import sys

input = sys.stdin.readline


def BFS():
    while q:
        x, y = q.popleft()

        for idx in range(len(dxy)):
            dx = x + dxy[idx][0]
            dy = y + dxy[idx][1]
            if 0 <= dx < m and 0 <= dy < n:
                if box[dx][dy] == 0:
                    box[dx][dy] = box[x][y] + 1
                    q.append([dx, dy])


dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]

n, m = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(m)]
q = deque()

for i in range(m):
    for j in range(n):
        if box[i][j] == 1:
            q.append([i, j])

BFS()

z = 1
res = -1

for b in box:
    for n in b:
        if n == 0:
            z = 0
        res = max(res, n)

if z == 0:
    print(-1)
elif res == 1:
    print(0)
else:
    print(res -1)