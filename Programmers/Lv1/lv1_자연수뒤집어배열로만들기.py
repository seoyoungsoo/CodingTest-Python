# 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = []
    a = n

    while a > 0:
        b = a % 10
        a = a // 10
        answer.append(b)

    return answer


# testcase 1
n = 404400123
print(solution(n))
