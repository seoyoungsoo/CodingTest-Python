# x만큼 간격이 있는 n개의 숫자

# 나의 풀이
def solution(x, n):
    answer = []

    for i in range(1, n + 1):
        answer.append(x * i)

    return answer


# 다른 풀이
def otherSol(x, n):
    return [i * x + x for i in range(n)]


# testcase1
x = 2
n = 5
print(solution(x, n))
print(otherSol(x, n))