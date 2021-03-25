# 9094번 수학적 호기심
# PyPy3로 채점할 때만 메모리 통과

tk = int(input())

for i in range(tk):
    cnt = 0
    n, m = map(int, input().split())

    for a in range(1, n-1):
        for b in range(a+1, n):
            if ((a * a + b * b) + m) % (a * b) == 0:
                cnt += 1
    print(cnt)