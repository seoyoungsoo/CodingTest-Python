# 7568번 덩치
import sys
input = sys.stdin.readline

N = int(input())
man, rank = [0 for _ in range(N)], [0 for _ in range(N)]

for i in range(N):
    w, h = map(int, input().split())
    man[i] = [w, h]

for i in range(N):
    cnt = 1
    w1, h1 = man[i][0], man[i][1]
    for j in range(N):
        w2, h2 = man[j][0], man[j][1]
        if w1 < w2 and h1 < h2:
            cnt += 1
    rank[i] = cnt

for n in rank:
    print(n, end=' ')