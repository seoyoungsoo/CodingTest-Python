# 2422번 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# 나의 풀이 3
# 시간 소모를 줄이기 위해 배열에 append가 아닌
# 2차원 배열 인덱스에 값을 넣어주는 방식으로 변경했다.
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
cnt = 0
if N < 3:
    print(cnt)
else:
    iceList = [[0 for _ in range(N+1)] for _ in range(N + 1)]

    for _ in range(M):
        n1, n2 = map(int, input().split())

        iceList[n1][n2], iceList[n2][n1] = 1, 1

    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if not iceList[i][j]:
                for k in range(j + 1, N + 1):
                    if not iceList[i][k] and not iceList[j][k]:
                        cnt += 1
    print(cnt)


# 나의 풀이 1
# combinations를 활용하여 풀어보려 했으나 시간 초과
'''from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
ice = [i for i in range(1, N + 1)]
iceList = deque(combinations(ice, 3))

for _ in range(M):
    comList = deque()
    n1, n2 = map(int, input().split())

    while iceList:
        cn = iceList.popleft()
        if n1 in cn and n2 in cn:
            continue
        else:
            comList.append(cn)
    iceList = comList

print(len(iceList))'''

# 나의 풀이 2
# 통과는 하지만 시간 소모가 크다
'''
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
cnt = 0
if N < 3:
    print(cnt)
else:
    iceList = [[] for _ in range(N + 1)]

    for _ in range(M):
        n1, n2 = map(int, input().split())

        if n2 not in iceList[n1]:
            iceList[n1].append(n2)
        if n1 not in iceList[n2]:
            iceList[n2].append(n1)

    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if j not in iceList[i]:
                for k in range(j + 1, N + 1):
                    if k not in iceList[i] and k not in iceList[j]:
                        cnt += 1
    print(cnt)'''