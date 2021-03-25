# 2635번 수 이어가기
import sys

input = sys.stdin.readline

N = int(input())
start, end = (N // 2) + 1, N

num = list()
while start <= end:
    tmp = [N, start]
    while True:
        tmp.append(tmp[-2] - tmp[-1])
        if tmp[-1] > tmp[-2]:
            break
        if tmp[-1] < 0:
            tmp[-1] = abs(tmp[-1])
            break
    if len(tmp) > len(num):
        num = tmp
    start += 1
print(len(num))
print(*num)