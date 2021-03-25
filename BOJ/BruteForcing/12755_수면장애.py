# 12755번 수면 장애

N = int(input())

i = 0
while N > 0:
    i += 1
    N -= len(str(i))

if N <= 0:
    print(str(i)[N-1])