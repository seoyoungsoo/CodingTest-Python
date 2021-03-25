# 2729번 이진수 덧셈

T = int(input())

for _ in range(T):
    a, b = map(str, input().split())

    n = int(a, 2) + int(b, 2)

    print(format(n, 'b'))