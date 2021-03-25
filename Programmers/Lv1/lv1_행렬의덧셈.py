# 행렬의 덧셈

# 나의 풀이
def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        sumArr = []
        for j in range(len(arr1[i])):
            sumArr.append(arr1[i][j] + arr2[i][j])
        answer.append(sumArr)

    return answer


# 다른 풀이
def otherSol(arr1, arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return answer


# testcase1
arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]
print(solution(arr1, arr2))
print(otherSol(arr1, arr2))
