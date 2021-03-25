# 11047번 동전 0
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = sorted(list(int(input()) for _ in range(N)), reverse=True)

cnt = 0
for c in coin:
    if K // c:
        cnt += K // c
        K = K % c
print(cnt)