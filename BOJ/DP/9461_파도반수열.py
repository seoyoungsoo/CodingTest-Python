# 9461번 파도반 수열

def cal(num):
    if num > len(p):
        for n in range(len(p), num):
            p.append(p[n - 3] + p[n - 2])
    print(p[num - 1])


p = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

n = int(input())
for i in range(n):
    num = int(input())
    cal(num)
