# 같은 숫자는 싫어

def solution(arr):
    answer = []
    equalNum = arr[0]

    answer.append(equalNum)

    for i in arr:
        if i == equalNum:
            continue
        else:
            answer.append(i)
            equalNum = i

    return answer


# testcase 1
arr = [1, 1, 3, 3, 0, 1, 1]
print(solution(arr))
