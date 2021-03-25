# 2018번 수들의 합

# 나의 풀이
N = int(input())

cnt = 1  # 자기 자신은 무조건 성립

for i in range(0, N - 1):
    tmp = 0
    for j in range(i + 1, N):
        if tmp == N:
            cnt += 1
            break
        elif tmp > N:
            break
        else:
            tmp += j
print(cnt)

# 투 포인터로 문제 푸는 방법
# 코드 참조: https://baby-ohgu.tistory.com/11
