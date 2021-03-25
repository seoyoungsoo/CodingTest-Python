# 6236번 용돈 관리
# 코드참조: https://ahn3330.tistory.com/87
# 문제설명: https://blog.naver.com/crm06217/222019416769
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
draw = [int(input()) for i in range(N)]

s, e = 1, sum(draw)
res = sum(draw)

while s <= e:
    m = (s + e) // 2
    cnt, money = 0, 0
    flag = False

    for d in draw:
        if m - d < 0:
            flag = True
            break
        elif money - d < 0:
            money = m
            cnt += 1
        money -= d

    if not flag:
        if cnt <= M:
            e = m - 1
            if m < res:
                res = m
        else:
            s = m + 1
    else:
        s = m + 1

print(res)
