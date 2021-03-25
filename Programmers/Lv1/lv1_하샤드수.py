# 하샤드 수

def solution(x):
    arr = 0
    for idx in str(x):
        arr += int(idx)

    return True if x % arr == 0 else False


# testcase1
x = 10
print(solution(x))