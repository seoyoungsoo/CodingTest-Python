# 14720번 우유 축제
# 0은 딸기우유, 1은 초코우유, 2는 바나나우유

n = int(input())
milk = list(map(int, input().split()))

drink, count = 0, 0
for taste in milk:
    if drink == taste:
        count += 1
        drink += 1
    if drink == 3:
        drink = 0

print(count)