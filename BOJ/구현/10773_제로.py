# 10773번 제로
import sys
input = sys.stdin.readline

K = int(input())
lst = []

for i in range(K):
    num = int(input())

    if not num:
        lst.pop()
    else:
        lst.append(num)

if not len(lst):
    print(0)
else:
    print(sum(lst))