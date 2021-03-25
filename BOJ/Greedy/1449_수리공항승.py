# 1449번 수리공 항승

N, L = map(int, input().split())
leak = sorted(list(map(int, input().split())))

tape = L - 1
res = 0
for i in range(N-1):
    if tape < leak[i+1] - leak[i]:
        res += 1
        tape = L - 1
    else:
        tape -= leak[i+1] - leak[i]
print(res+1)