# 2720번 세탁소 사장 동혁
import sys
input = sys.stdin.readline

money = [25, 10, 5, 1]

T = int(input())

for _ in range(T):
    change = []
    coin = int(input())

    for m in money:
        change.append(coin // m)
        coin %= m

    print(' '.join(map(str, change)))