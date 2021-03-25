# 18310번 안테나
import sys

input = sys.stdin.readline

N = int(input())
house = sorted(list(map(int, input().split())))

# 집의 개수가 홀수일 경우 가운데에 존재하는 집이 정답
# 집의 개수가 짝수일 경우 가운데에 존재하는 2개의 집 중 숫자가 작은 집이 정답
mid = (len(house) - 1) // 2

print(house[mid])
