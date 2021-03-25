# 11866번 요세푸스 문제 0

N, K = map(int, input().split())
q = [i for i in range(1, N + 1)]

idx = 0
res = list()
while q:
    idx += (K - 1)
    if idx > len(q) - 1:
        idx %= len(q)
    res.append(q.pop(idx))
print('<' + str(res)[1:-1] + '>')