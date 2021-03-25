# 피보나치 수
"""
참조 링크
https://programmers.co.kr/questions/11991
"""


# 나의 풀이
def solution(n):
    Fibo = [0 for x in range(n + 1)]
    Fibo[1] = 1
    for i in range(2, n + 1):
        Fibo[i] = (Fibo[i - 1] + Fibo[i - 2]) % 1234567
    return Fibo[n]


# 다른 풀이
# 위의 풀이보다 메모리 효율성이 좋다.
def otherSol(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a % 1234567


# testcase1
n = 3000
print(solution(n))
print(otherSol(n))
