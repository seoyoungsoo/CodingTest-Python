# 숫자의 표현

# 나의 풀이
def solution(n):
    answer = 0
    for i in range(1, n+1):
        tmp = 0
        for j in range(i, n+1):
            tmp += j
            if tmp > n:
                break
            elif tmp == n:
                answer += 1

    return answer


# testcase1
n = 15
print(solution(n))