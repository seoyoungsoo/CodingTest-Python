# 2293번 동전 1
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
dp = [0 for _ in range(k + 1)]
dp[0] = 1

for _ in range(n):
    coins.append(int(input()))

coins = list(set(coins))

for coin in coins:
    for i in range(1, k+1):
        if i - coin >= 0:
            dp[i] += dp[i - coin]

print(dp[k])