# 체육복

def solution(n, lost, reserve):
    for i in range(n + 1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)

    for i in range(n + 1):
        if i in lost:
            if i - 1 in reserve:
                lost.remove(i)
                reserve.remove(i - 1)
            elif i + 1 in reserve:
                lost.remove(i)
                reserve.remove(i + 1)
    return n - len(lost)


n = 5
lost = [2, 4]
reserve = [1, 3, 5]

print(solution(n, lost, reserve))
