# 1495번 기타리스트
# 코드참조: https://deok2kim.tistory.com/80

n, s, m = map(int, input().split())
song = list(map(int, input().split()))
dp = [[0] * (m + 1) for _ in range(n + 1)]

dp[0][s] = 1

for i in range(1, n + 1):
    for j in range(m + 1):
        if dp[i - 1][j]:
            if j + song[i - 1] <= m:
                dp[i][j + song[i - 1]] = 1
            if j - song[i - 1] >= 0:
                dp[i][j - song[i - 1]] = 1

for idx in range(m, -1, -1):
    if dp[-1][idx] == 1:
        print(idx)
        exit(0)
else:
    print(-1)
