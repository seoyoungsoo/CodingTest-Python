# 11399번 ATM

n = int(input())
p = sorted(list(map(int, input().split())))

time = 0
tmp = 0
for i in p:
    tmp += time + i
    time = time + i

print(tmp)