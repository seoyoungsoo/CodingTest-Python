# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()

    return answer


# testcase 1
arr = [5, 9, 7, 10]
divisor = 5
print(solution(arr, divisor))
