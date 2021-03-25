# 2512번 예산

# while s < e에 else s = m 일 경우 시간초과
# 아래의 경우 시간초과에 걸리지 않는다.
import sys
input = sys.stdin.readline

N = int(input())
req = list(map(int, input().split()))
N = int(input())

s, e = 0, max(req)
while s <= e:
    m = (s + e) // 2
    tmp = 0
    for i in req:
        if i > m:
            tmp += m
        else:
            tmp += i
    if tmp > N:
        e = m - 1
    else:
        s = m +1
print(e)