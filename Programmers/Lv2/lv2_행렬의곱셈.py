# 행렬의 곱셈

# 나의 풀이
def solution(arr1, arr2):
    # ex) 3 x 2 행렬과 2 x 4 행렬을 곱하면 3 x 4 행렬이 됨을 알아야 함
    answer = [[0 for col in range(len(arr2[0]))] for row in range(len(arr1))]

    for i, v1 in enumerate(arr1):
        for k, v2 in enumerate(v1):
            for j in range(len(arr2[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer


# 다른 풀이
def otherSol(arr1, arr2):
    answer = [[sum(a*b for a, b in zip(x_row, y_col))for y_col in zip(*arr2)]for x_row in arr1]
    return answer


# testcase1
arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1, arr2))
print(otherSol(arr1, arr2))