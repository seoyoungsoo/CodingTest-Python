# 약수의 합

def solution(n):
    dSum = 0

    for i in range(1, n + 1):
        if n % i == 0:
            dSum += i

    return dSum


# testcase1
n = 12
print(solution(n))
