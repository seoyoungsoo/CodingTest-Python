# 2670번 연속부분최대곱
import sys

n = int(sys.stdin.readline())
farr = [0 for _ in range(n)]
for k in range(n):
    farr[k] = float(sys.stdin.readline())

tmp = [0 for _ in range(n)]
for i in range(n):
    mul = 1
    for j in range(i, n):
        mul = mul * farr[j]
        if tmp[i] < mul:
            tmp[i] = mul
        elif mul < 1:
            break
print(format(max(tmp), '.3f'))