# 1009번 분산처리
# 코드 참조: https://pacific-ocean.tistory.com/336

num = [[], [1], [6, 2, 4, 8], [1, 3, 9, 7], [6, 4], [5], [6], [1, 7, 9, 3], [6, 8, 4, 2], [1, 9]]
T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    a = int(str(a)[-1])

    if a:
        print(num[a][b % len(num[a])])
    else:
        print(10)