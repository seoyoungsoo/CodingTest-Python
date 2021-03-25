# 2003번 수들의 합 2

N, M = map(int, input().split())
num = list(map(int, input().split()))

start, end = 0, 1
now = num[start]
res = 0
if now == M:
    res += 1

while start < N:
    if now < M and end < N:
        now += num[end]
        end += 1
    else:
        now -= num[start]
        start += 1

    if now == M:
        res += 1
print(res)