# 2217번 로프

# 나의 풀이
# 통과했지만 걸린 시간이 3696ms가 나와 시간을 줄일 방법을 생각했다.
# 문제는 input()의 시간이였다.
# sys.stdin.readline()을 사용한 경우 152ms의 시간이 걸리는 것을 확인
# 많은 양의 입력을 받을 때 sys.stdin.readline()을 사용하면 시간이 단축된다.
import sys
input = sys.stdin.readline

n = int(input())
rope = [0 for _ in range(n)]
maxWeight = 0

for i in range(n):
    rope[i] = int(input())
rope.sort(reverse=True)

while rope:
    tmp = len(rope) * rope.pop()
    if tmp > maxWeight:
        maxWeight = tmp
print(maxWeight)

# 간소화 방법
'''
n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort()
maxWeight = 0
for i in range(n):
    maxWeight = max(maxWeight, rope[i]*(n-i))
print(maxWeight)
'''