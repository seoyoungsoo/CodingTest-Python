# 1890번 점프
# 코드참조: https://deok2kim.tistory.com/189

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            print(dp[i][j])
            exit(0)

        crnt = board[i][j]

        if i + crnt < n:
            dp[i + crnt][j] += dp[i][j]
        if j + crnt < n:
            dp[i][j + crnt] += dp[i][j]