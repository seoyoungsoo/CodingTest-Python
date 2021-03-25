# 코드참조: https://new93helloworld.tistory.com/221

n, m = map(int, input().split())
store = [list(map(int, input().split())) for _ in range(m)]

dp = [[0] * n for _ in range(m)]
dp[0][0] = store[0][0]

for i in range(m):
    for j in range(n):
        dp[i][j] = store[i][j] + max(dp[i-1][j], dp[i][j-1])
print(max(dp[-1]))