# 1783번 병든 나이트
# 코드 참조: https://dirmathfl.tistory.com/223

n, m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m+1) // 2))
elif m < 7:
    print(min(4, m))
else:
    print(m - 7 + 5)