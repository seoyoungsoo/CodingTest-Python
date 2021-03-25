# 1920번 수 찾기

N = input()
arr_N = set(input().split(' '))
M = input()
arr_M = list(input().split(' '))

for i in arr_M:
    if i not in arr_N:
        print(0)
    else:
        print(1)