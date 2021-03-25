# 1149번 RGB거리
import sys
input = sys.stdin.readline

N = int(input())
rgb = [0 for _ in range(N)]

for idx in range(N):
    rgb[idx] = list(map(int, input().split()))

for i in range(1, N):
    # 빨간 집
    rgb[i][0] += min(rgb[i-1][1], rgb[i-1][2])

    # 초록 집
    rgb[i][1] += min(rgb[i-1][0], rgb[i-1][2])

    # 파란 집
    rgb[i][2] += min(rgb[i-1][0], rgb[i-1][1])

print(min(rgb[-1]))