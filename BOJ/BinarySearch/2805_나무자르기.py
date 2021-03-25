# 2805번 나무자르기
# Python3로 시간초과, PyPy3로 제출 시 통과했다.
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

s, e = 1, max(tree)
maxL = 0

while s <= e:
    m = (s + e) // 2
    tmp = 0
    for i in tree:
        if i > m:
            tmp += i - m
    if tmp >= M:
        if maxL < m:
            maxL = m
        s = m + 1
    else:
        e = m - 1
print(maxL)