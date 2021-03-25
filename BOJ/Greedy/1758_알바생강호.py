# 1758번 알바생 강호
import sys
input = sys.stdin.readline

N = int(input())
pay = sorted([int(input()) for _ in range(N)], reverse=True)
res = 0

for idx, v in enumerate(pay):
    tip = v - idx
    if tip > 0:
        res += tip
print(res)