# 1931번 회의실 배정
import sys
input = sys.stdin.readline

N = int(input())
conf = [0] * N

for i in range(N):
    conf[i] = list(map(int, input().split()))

conf.sort(key=lambda x: (x[1], x[0])) # 리스트의 1번째 인덱스 순으로 먼저 정렬한 후 같은 값이 있을 경우 0번째 인덱스 순으로 다시 정렬함

total = 1
tmp = conf[0][1]
for j in range(1, N):
    if tmp <= conf[j][0]:
        total += 1
        tmp = conf[j][1]
print(total)