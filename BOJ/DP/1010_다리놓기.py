# 1010번 다리 놓기

# 조합을 구현하기 위해 팩토리얼 함수 구현
# 조합의 공식은 n! / (n-r)! * r!
def factorial(n):
    tmp = 1
    for i in range(n, 0, -1):
        tmp *= i
    return tmp


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    if n == m:
        print(1)
    else:
        bridge = int(factorial(m) / (factorial(m - n) * factorial(n)))
        print(bridge)

# 팩토리얼을 사용하지 않는 코드
'''for _ in range(t):
    n, m = map(int, input().split())
    answer = 1
    k = m - n

    while n > k:
        answer *= m
        m -= 1
    while m > 1:
        answer = answer // n
        n -= 1

    print(answer)'''