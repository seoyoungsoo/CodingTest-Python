# 11722번 가장 긴 감소하는 부분 수열
import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if seq[i] < seq[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))