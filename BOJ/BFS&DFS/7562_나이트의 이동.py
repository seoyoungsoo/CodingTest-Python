# 7562번 나이트의 이동
from collections import deque
import sys

input = sys.stdin.readline


def BFS(nx, ny, px, py):
    q = deque()
    q.append((nx, ny))
    board[nx][ny] = 1

    while q:
        a, b = q.popleft()
        if a == px and b == py:
            return board[px][py] - 1
        for i in range(len(move)):
            x = a + move[i][0]
            y = b + move[i][1]
            if 0 <= x < L and 0 <= y < L and board[x][y] == 0:
                board[x][y] = board[a][b] + 1
                q.append((x, y))


move = [[-2, -1], [-1, -2], [-2, 1], [-1, 2], [1, -2], [2, -1], [2, 1], [1, 2]]
T = int(input())

for _ in range(T):
    L = int(input())
    board = [[0] * L for _ in range(L)]
    nx, ny = map(int, input().split())
    px, py = map(int, input().split())

    res = BFS(nx, ny, px, py)
    print(res)