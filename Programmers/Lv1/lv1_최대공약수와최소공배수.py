# 최대공약수와 최소공배수

# 나의 풀이
def solution(n, m):
    answer = []

    if n < m:
        minV = n
        maxV = m
    else:
        minV = m
        maxV = n

    for i in range(minV + 1, 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break

    for i in range(maxV, (n * m) + 1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break

    return answer


# 다른 풀이
def otherSol(n, m):
    a, b = max(n, m), min(n, m)
    t = 1
    while t > 0:
        t = a % b
        a, b = b, t
    answer = [a, int(n*m/a)]

    return answer


# testcase1
n = 3
m = 12
print(solution(n, m))
print(otherSol(n, m))
