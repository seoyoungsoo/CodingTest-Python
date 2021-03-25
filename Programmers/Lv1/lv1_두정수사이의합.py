# 두 정수 사이의 합

def solution(a, b):
    num = 0
    if a == b:
        return a
    if a > b:
        for i in range(b, a + 1):
            num += i
        return num
    else:
        for i in range(a, b + 1):
            num += i
        return num


# testcase 1
a, b = 3, 5
print(solution(a, b))
