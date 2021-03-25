# 1138번 한 줄로 서기
# 코드참조: https://fullmoon1344.tistory.com/79

N = int(input())
man = list(map(int, input().split()))
res = [0] * N

for i in range(N):
    zero = 0
    for j in range(N):
        if zero == man[i] and res[j] == 0:
            res[j] = i + 1
            break
        elif res[j] == 0:
            zero += 1
print(*res)