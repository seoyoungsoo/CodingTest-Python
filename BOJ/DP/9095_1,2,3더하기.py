# 9095번 1,2,3 더하기

T = int(input())

for _ in range(T):
    dp = [0, 1, 2, 4]
    n = int(input())

    if n <= 3:
        print(dp[n])
    else:
        for i in range(4, n + 1):
            dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
        print(dp[-1])
