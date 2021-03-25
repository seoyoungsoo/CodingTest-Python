# 2750번 수 정렬하기
import sys

input = sys.stdin.readline

N = int(input())
numList = sorted([int(input()) for _ in range(N)])

for i in range(N):
    print(numList[i])