# 2178번 미로 탐색
from collections import deque
import sys

input = sys.stdin.readline


def BFS(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1

    while q:
        x, y = q.popleft()
        for i in range(len(dxy)):
            dx = x + dxy[i][0]
            dy = y + dxy[i][1]
            if 0 <= dx < N and 0 <= dy < M:
                if maze[dx][dy] == 1 and visited[dx][dy] == 0:
                    visited[dx][dy] = visited[x][y] + 1
                    q.append([dx, dy])


N, M = map(int, input().split())
# input()의 마지막은 줄바꿈을 나타내는 '\n'가 들어가므로 input()[:-1]의 값을 리스트에 넣는다.
maze = [list(map(int, input()[:-1])) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 시작 위치는 0,0이다.
# 도착 위치는 N-1, M-1이다.
BFS(0, 0)
print(visited[N-1][M-1])