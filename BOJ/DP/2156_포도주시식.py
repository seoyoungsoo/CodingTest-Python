# 2156번 포도주 시식
# 코드참조: https://inspirit941.tistory.com/284

# dp[위치] = 해당 위치까지 왔을 때 마실 수 있는 최댓값
# i-1, i-2 둘 다 마신 경우 = 3잔 연속 마실 수 없으므로 dp[i-1]
# i-1잔을 마시지 않는 경우 = dp[i-2] + wine[i]
# i-2잔을 마시지 않는 경우 = dp[i-3] + wine[i-1] + wine[i]

import sys
input = sys.stdin.readline

wine = [0, 0, 0]
n = int(input())
for _ in range(n):
    wine.append(int(input()))

dp = [0] * len(wine)
for i in range(3, n+3):
    dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])

print(dp[-1])