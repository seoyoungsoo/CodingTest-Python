# 2503번 숫자 야구
from itertools import permutations
import sys

input = sys.stdin.readline

N = int(input())
num = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

for _ in range(N):
    ask, strike, ball = map(int, input().split())
    ask = list(str(ask))
    r_cnt = 0

    for i in range(len(num)):
        s_cnt = b_cnt = 0
        i -= r_cnt

        for j in range(3):
            tmp = int(ask[j])
            if tmp in num[i]:
                if j == num[i].index(tmp): # index 함수로 tmp 값이 존재하는 인덱스를 알 수 있다.
                    s_cnt += 1
                else:
                    b_cnt += 1

        if s_cnt != strike or b_cnt != ball:
            num.remove(num[i])
            r_cnt += 1
print(len(num))