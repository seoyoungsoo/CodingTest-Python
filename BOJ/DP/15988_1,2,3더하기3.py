# 15988번 1, 2, 3 더하기 3
import sys

input = sys.stdin.readline

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for k in range(int(input())):
    print(dp[int(input())])
