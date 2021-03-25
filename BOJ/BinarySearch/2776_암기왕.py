# 2776번 암기왕
# 이런 문제를 풀 때 3가지의 경우의 수가 존재한다.
# 1. 리스트를 정렬한 후 binary search 로 탐색
# 2. set(집합) 자료구조를 이용
# 3. hash 자료구조를 이용
# 해당 문제는 카운팅이 필요하지 않아 set 자료구조를 사용하는 것이 좋다.
# binary search 로 문제를 풀어보려 했으나 시간초과에 걸림
# set 은 이진트리로 구현되어 있어 탐색의 시간복잡도가 O(log n)이라 시간초과에 걸리지 않는 듯
import sys

input = sys.stdin.readline

'''def BS(n):
    start, end = 0, N-1

    while start <= end:
        mid = (start + end) // 2
        if n == note1[mid]:
            return 1

        if note1[mid] > n:
            end = mid
        else:
            start = mid + 1
    return 0'''

T = int(input())

for _ in range(T):
    N = int(input())
    note1 = set(list(map(int, input().split())))
    M = int(input())
    note2 = list(map(int, input().split()))

    for n in note2:
        if n in note1:
            print(1)
        else:
            print(0)
