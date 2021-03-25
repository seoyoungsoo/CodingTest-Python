# 15990번 1, 2, 3 더하기 5
# 코드참조: https://hooongs.tistory.com/224

dp = [[0] * 4 for _ in range(100001)]

dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]

mod = 1000000009

for i in range(4, 100001):
    for j in range(1, 4):
        dp[i][j] = (sum(dp[i-j]) - dp[i-j][j]) % mod

t = int(input())

for _ in range(t):
    n = int(input())
    print(sum(dp[n]) % mod)