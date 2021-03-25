# 11060번 점프 점프
# 코드참조: https://lem0nad3.tistory.com/6

import sys
input = sys.stdin.readline

n = int(input())
maze = list(map(int, input().split()))

dp = [1001] * n
dp[0] = 1

for i in range(0, n):
    j = maze[i]
    for k in range(i+1, i+j+1):
        if k < n:
            dp[k] = min(dp[k], dp[i]+1)

if dp[n-1] > 1000:
    print(-1)
else:
    print(dp[n-1] - 1)