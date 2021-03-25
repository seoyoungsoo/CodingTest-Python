# 1057번 토너먼트
import sys

input = sys.stdin.readline

n, kim, lim = map(int, input().split())

idx = 1
while True:
    n1 = kim if kim % 2 == 0 else kim + 1
    n2 = lim if lim % 2 == 0 else lim + 1

    if n1 == n2:
        print(idx)
        break
    kim = n1 // 2
    lim = n2 // 2
    idx += 1