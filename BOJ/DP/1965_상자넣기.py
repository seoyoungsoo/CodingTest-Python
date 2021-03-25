# 1965번 상자넣기

n = int(input())
box = list(map(int, input().split()))
collect = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if box[i] > box[j]:
            collect[i] = max(collect[i], collect[j]+1)
print(max(collect))