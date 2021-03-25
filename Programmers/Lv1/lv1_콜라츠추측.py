# 콜라츠 추측

def solution(num):
    count = 0

    while num != 1:
        if num % 2:
            num = num * 3 + 1
        else:
            num = num / 2
        count += 1
        if count == 500:
            return -1

    return count


# testcase1
n = 6
print(solution(n))