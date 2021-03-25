# 3진법 뒤집기

# 나의 풀이
THREE = 3


def solution(n):
    question = []
    answer = 0
    decimal = n

    while True:
        if decimal > 0:
            modular = decimal % THREE
            question.append(modular)
            decimal //= THREE
        else:
            break

    sqrNum = 0
    for x in range(len(question)-1, -1, -1):
        answer += int(question[x]) * (3**sqrNum)
        sqrNum += 1

    return answer


# testcase 1
n = 45
print(solution(n))