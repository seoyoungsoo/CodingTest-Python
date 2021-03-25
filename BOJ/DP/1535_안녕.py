# 1535번 안녕
# 코드참조: https://sangminlog.tistory.com/entry/boj-1535

n = int(input())

loss_hp = list(map(int, input().split()))
get_happy = list(map(int, input().split()))

dp = [[0] * 101 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(100):
        if j >= loss_hp[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-loss_hp[i-1]] + get_happy[i-1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][-2])