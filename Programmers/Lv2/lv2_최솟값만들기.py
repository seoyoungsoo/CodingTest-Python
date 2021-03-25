# 최솟값 만들기

# 나의 풀이
# 두 수를 곱한 값을 누적한 값이 최소가 되려면
# 두 배열의 최소값 x 최대값을 하면 성립이 됨
def solution(A, B):
    tmp = 0
    A.sort(reverse=True)
    B.sort()

    for a, b in zip(A, B):
        tmp += a * b
    return tmp


# testcase1
A = [1, 4, 2]
B = [5, 4, 4]
print(solution(A, B))
