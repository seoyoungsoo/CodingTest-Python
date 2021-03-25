# 13410번 거꾸로 구구단
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dan = [0] * (K+1)

for i in range(1, K+1):
    num = str(N * i)
    dan[i] = int(num[::-1])
print(max(dan))