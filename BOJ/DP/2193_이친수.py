# 2193번 이친수

n = int(input())

a, b = 0, 1

if n <= 2:
    print(1)
else:
    for i in range(n):
        a, b = b, a + b

    print(a)
