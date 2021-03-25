# 2847번 게임을만든봉준이

n = int(input())
score = [int(input()) for _ in range(n)]

res = 0
for i in range(len(score)-2, -1, -1):
    if score[i] >= score[i+1]:
        res += score[i] - score[i+1] + 1
        score[i] = score[i+1] - 1
print(res)