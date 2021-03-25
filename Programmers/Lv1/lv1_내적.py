# 내적

def solution(a, b):
    inner_product = 0  # 내적

    for i in range(0, len(a)):
        inner_product += a[i] * b[i]

    return inner_product


# testcase1
a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]

print(solution(a, b))
