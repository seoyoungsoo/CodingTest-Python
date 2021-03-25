# 소수 찾기

# itertools를 이용한 문제
# 나의 풀이
from itertools import permutations


def prime(n):  # 소수일 경우 True, 아닐 경우 False를 return
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = []

    for i in range(1, len(numbers) + 1):
        perlist = list(map(''.join, permutations(numbers, i)))
        for j in list(set(perlist)):
            if prime(int(j)):
                answer.append(int(j))

    return len(set(answer))


# 다른 풀이
# 비트 연산자를 잘 이해하자
def otherSol(numbers):
    a = set()
    for i in range(len(numbers)):
        a |= set(map(int, map(''.join, permutations(numbers, i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))

    return len(a)


# testcase1
numbers = '17'
print(solution(numbers))
print(otherSol(numbers))