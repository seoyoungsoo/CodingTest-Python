# 4641번 Doubles
import sys
input = sys.stdin.readline

while True:
    lst = sorted(list(map(int, input().split())))
    if len(lst) == 1:
        break

    cnt = 0
    for i in range(1, len(lst)):
        if lst[i] * 2 in lst:
            cnt += 1
    print(cnt)