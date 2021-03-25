# 2231번 분해합

n = int(input())
for i in range(1, n + 1):
    num_list = list(map(int, str(i)))
    sum_num = i + sum(num_list)
    if sum_num == n:
        print(i)
        break
else:
    print(0)
