# 1654번 랜선자르기
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
line = [int(input()) for _ in range(k)]

s, l = 1, max(line)
answer = 0
while s <= l:
    m = (s + l) // 2
    tmp = 0
    for i in line:
        tmp += i // m
    if tmp < n:
        l = m - 1
    else:
        if answer < m:
            answer = m
        s = m + 1
print(answer)