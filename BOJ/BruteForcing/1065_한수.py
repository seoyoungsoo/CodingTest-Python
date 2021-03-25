# 1065번 한수
import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for i in range(1, N+1):
    if len(str(i)) <= 2:
        cnt += 1
    else:
        seq = str(i)
        tmp = int(seq[-1]) - int(seq[-2])
        for j in range(len(seq)-3, -1, -1):
            if tmp != int(seq[j+1]) - int(seq[j]):
                break
        else:
            cnt += 1
print(cnt)