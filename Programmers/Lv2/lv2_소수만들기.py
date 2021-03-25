# 소수 만들기

# 나의 풀이
# combinations를 이용해서 배열의 개수가 많아지면 효율성이 낮아질 것이라 생각함
from itertools import combinations


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(nums):
    cnt = 0
    for i in list(combinations(nums, 3)):
        if prime(sum(i)):
            cnt += 1

    return cnt


# 다른 풀이
# for else 문을 알아보자
def otherSol(nums):
    answer = 0
    for a in combinations(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand % j == 0:
                break
        else:
            answer += 1

    return answer


# testcase1
nums = [1, 2, 3, 4]
print(solution(nums))
print(otherSol(nums))