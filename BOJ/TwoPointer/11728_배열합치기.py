# 11728번 배열 합치기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*sorted(A+B))