# 정수 제곱근 판별

# math 라이브러리 사용
import math


def solution(n):
    x = int(math.sqrt(n))

    return ((x + 1) ** 2) if x ** 2 == n else -1


# math 라이브러리 미사용
def otherSol(n):
    x = n ** 0.5

    return int(((x + 1) ** 2) if x ** 2 == n else -1)


# testcase 1
n = 121
n2 = 3
print(solution(n))

print(otherSol(n2))
