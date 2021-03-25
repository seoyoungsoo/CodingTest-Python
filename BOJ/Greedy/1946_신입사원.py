# 1946번 신입 사원
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    emp = [0 for _ in range(N)]

    for i in range(N):
        emp[i] = list(map(int, input().split()))

    emp.sort()
    cnt = 1
    cmp = emp[0][1]

    for i in range(1, N):
        if cmp > emp[i][1]:
            cnt += 1
            cmp = emp[i][1]
    print(cnt)