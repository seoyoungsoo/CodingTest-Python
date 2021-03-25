# 9625번 BABBA

k = int(input())

if k == 0:
    print("1 0")
elif k == 1:
    print("0 1")
else:
    if k == 2:
        print("1 1")
    else:
        a, b = 1, 1
        for i in range(k-2):
            a, b = b, a+b

        print(a, b)