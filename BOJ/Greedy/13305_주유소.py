# 13305번 주유소
# 코드 참조: https://alpyrithm.tistory.com/134

N = int(input())
road = list(map(int, input().split()))
pay = list(map(int, input().split()))

res = 0
m = pay[0]
for i in range(N-1):
    if pay[i] < m:
        m = pay[i]
    res += m * road[i]
print(res)