# 1789번 수들의 합

N = int(input())

count = 0
tmp = 1
while True:
    N -= tmp

    if N >= 0:
        count += 1
        tmp += 1
    else:
        print(count)
        break
