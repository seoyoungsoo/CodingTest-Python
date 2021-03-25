# 2303번 숫자 게임
from itertools import combinations
import sys

input = sys.stdin.readline

N = int(input())
lst = [[0, 0, 0] for _ in range(N)]

for i in range(N):
    card = list(map(int, input().split()))

    cardList = list(set(combinations(card, 3)))
    maxCard = list()
    for cl in cardList:
        first = (sum(cl)) % 10
        maxCard.append([i + 1, first])
    lst[i] = max(maxCard)

maxLst = 0
idx, num = list(), list()
for l in lst:
    if l[1] >= maxLst:
        maxLst = l[1]
        idx.append(l[0])
        num.append(l[1])

if len(idx) == 1:
    print(idx[0])
else:
    print(max(idx))
'''maxLst = 0
cnt, num = list(), list()
for idx, v in enumerate(lst):
    if v[0] >= maxLst:
        maxLst = v[0]
        cnt.append(idx+1)
        num.append(v[1])
print(lst)
print(cnt, num)
if len(cnt) == 1:
    print(cnt[0])
else:
    print(cnt[-1])'''
