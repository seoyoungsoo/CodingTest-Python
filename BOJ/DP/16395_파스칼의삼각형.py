# 16395번 파스칼의 삼각형

dp = [[1] * idx for idx in range(31)]

n, k = map(int, input().split())

if n >= 3:
    for i in range(3, n + 1):
        for j in range(1, len(dp[i])-1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
print(dp[n][k-1])