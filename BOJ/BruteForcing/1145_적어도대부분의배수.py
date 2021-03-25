# 1145번 적어도 대부분의 배수

numbers = sorted(list(map(int, input().split())))

m = numbers[0]

while True:
    cnt = 0
    for i in numbers:
        if m % i == 0:
            cnt += 1
    if cnt >= 3:
        print(m)
        break
    m += 1
