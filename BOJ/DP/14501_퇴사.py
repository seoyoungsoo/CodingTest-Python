# 14501번 퇴사
import sys

N = int(sys.stdin.readline())
term, pay = [0 for i in range(N)], [0 for i in range(N)]

for i in range(N):
    n1, n2 = map(int, sys.stdin.readline().split())
    term[i] = n1
    pay[i] = n2

benefit = [0] * (N+1)

for i in range(len(term)-1, -1, -1):
    if term[i] + i <= N:
        benefit[i] = max(pay[i]+benefit[i+term[i]], benefit[i+1])
    else:
        benefit[i] = benefit[i+1]
    print(benefit)