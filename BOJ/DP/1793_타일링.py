# 1793번 타일링

while True:
    try:
        n = int(input())
        dp = [1, 1, 3]

        if n < 3:
            print(dp[n])
        else:
            for i in range(3, n+1):
                dp.append(dp[i-1] + 2 * dp[i-2])

            print(dp[n])
    except EOFError:
        exit(0)