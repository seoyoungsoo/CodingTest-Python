# 카펫

# 나의 풀이
# 둘레를 이용한 풀이 방법
def solution(brown, yellow):
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            j = yellow // i
            if (i + j) * 2 + 4 == brown:
                return [j + 2, i + 2]


# 다른 풀이
# 근의 공식
def otherSol(brown, yellow):
    import math
    w = int(((brown + 4) / 2 + math.sqrt(((brown + 4) / 2) ** 2 - 4 * (brown + yellow))) / 2)
    h = int(((brown + 4) / 2 - math.sqrt(((brown + 4) / 2) ** 2 - 4 * (brown + yellow))) / 2)
    return [w, h]


# testcase1
brown = 24
yellow = 24
print(solution(brown, yellow))
print(otherSol(brown, yellow))