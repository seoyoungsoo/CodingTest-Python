# 두 개 뽑아서 더하기

def solution(numbers):
    answer = []
    result = []

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                answer.append(numbers[i] + numbers[j])

    answer = set(answer)  # 중복 제거
    result = list(answer)
    result.sort()

    return result


# testcase 1
numbers = [2, 1, 3, 4, 1]
print(solution(numbers))
