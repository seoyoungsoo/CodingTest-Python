# 정수 내림차순으로 배치하기

def solution(n):
    nList = list(str(n))
    nList.sort(reverse=True)

    return int("".join(nList))


# testcase1
n = 118372
print(solution(n))