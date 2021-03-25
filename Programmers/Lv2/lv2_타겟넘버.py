# 타겟 넘버

# 나의 풀이
# BFS를 활용한 풀이
def solution(numbers, target):
    arr = [numbers[0], -numbers[0]]

    for i in range(1, len(numbers)):
        tmp = []
        for j in arr:
            tmp.append(j + numbers[i])
            tmp.append(j - numbers[i])
        arr = tmp

    return arr.count(target)


# 다른 풀이1
# DFS를 활용한 풀이
def dfs(nums, i, n, t):
    ret = 0
    if i == len(nums):
        if n == t:
            return 1
        else:
            return 0
    ret += dfs(nums, i + 1, n + nums[i], t)
    ret += dfs(nums, i + 1, n - nums[i], t)
    return ret


def otherSol1(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer


# testcase1
numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
print(otherSol1(numbers, target))
