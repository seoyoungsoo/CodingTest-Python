# 14916번 거스름돈

n = int(input())

if n % 5 == 0:
    print(n // 5)
else:
    cnt = 0
    while n > 1:
        n -= 2
        cnt += 1
        if n % 5 == 0:
            cnt += n // 5
            n %= 5
            break

    if n:
        print(-1)
    else:
        print(cnt)
