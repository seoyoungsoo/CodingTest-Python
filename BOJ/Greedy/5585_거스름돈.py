# 5585번 거스름돈

money = [500, 100, 50, 10, 5, 1]

changes = 1000 - int(input())
cnt = 0

for i in money:
    if changes // i:
        cnt += changes // i
        changes %= i

print(cnt)