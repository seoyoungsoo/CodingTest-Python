# 2579번 계단 오르기
import sys
input = sys.stdin.readline

n = int(input())
floor = [0]
for _ in range(n):
    floor.append(int(input()))

if n == 1:
    print(floor[-1])
else:
    dp = [0] * (n + 1)

    dp[1] = floor[1]
    dp[2] = max(floor[2], floor[1] + floor[2])
    for i in range(3, n + 1):
        dp[i] = max(floor[i] + dp[i - 2], floor[i] + floor[i - 1] + dp[i - 3])
    print(dp[-1])