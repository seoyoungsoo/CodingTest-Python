# 1003번 피보나치 함수

T = int(input())


def fiboCal(num):
    zero = [1, 0, 1]
    one = [0, 1, 1]
    if num > 2:
        for i in range(2, num):
            zero.append(zero[i] + zero[i - 1])
            one.append(one[i] + one[i - 1])
    return zero[num], one[num]


for i in range(T):
    num = int(input())
    cnt0, cnt1 = fiboCal(num)
    print(cnt0, cnt1)
