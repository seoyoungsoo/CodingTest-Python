# 자릿수 더하기

def solution(n):
    answer = 0

    for i in str(n):
        answer += int(i)

    return answer


# 다른 풀이
def otherSol(n):
    return sum([int(i) for i in str(n)])


# testcase1
n = 123
print(solution(n))

print(otherSol(n))