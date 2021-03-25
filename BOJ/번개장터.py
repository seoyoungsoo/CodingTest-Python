from collections import deque

n, m = map(int, input().split())
dxy = [-1, 1]


def bfs(x, y):
    visited = [[-1] * n for _ in range(m)]
    visited[x][y] = 0
    q = deque()
    q.append([x, y])

    while q:
        num = q.popleft()
        dx = num[0]
        dy = num[1]
        if scroll[dx + 1][dy] == 'x':
            for j in range(2):
                ny = dy + dxy[j]
                if 0 <= ny < n and visited[dx][ny] == -1 and scroll[dx][ny] != 'x':
                    visited[dx][ny] = visited[dx][dy] + 1
                    q.append([dx, ny])
        else:
            if dx + 1 == m-1:
                visited[dx + 1][dy] = visited[dx][dy]
            else:
                visited[dx + 1][dy] = visited[dx][dy]
                q.append([dx + 1, dy])
    return max(visited[-1])


scroll = [list(map(str, input())) for _ in range(m)]
res = []

for i in range(n):
    if scroll[0][i] == 'c':
        res.append(bfs(0, i))

print(min(res))
