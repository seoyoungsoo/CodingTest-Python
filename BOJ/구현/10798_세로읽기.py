# 10798번 세로읽기

lst = [list(map(str, input())) for _ in range(5)]

maxLen = max(len(s) for s in lst)

for i in range(maxLen):
    for j in range(5):
        if len(lst[j]) > i:
            print(lst[j][i], end='')