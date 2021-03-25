# 14697번 방 배정하기
# 다양한 방법의 풀이 참조 https://skeo131.tistory.com/91

a, b, c, n = map(int, input().split())

dp = [0] * (300 + 1)
dp[a] = dp[b] = dp[c] = 1

for i in range(1, n+1):
    dp[i] = 1 if dp[i] or dp[i-a] or dp[i-b] or dp[i-c] else 0

print(dp[i])