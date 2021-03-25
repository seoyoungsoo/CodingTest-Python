# 제일 작은 수 제거하기

# 나의 풀이
def solution(arr):
    if len(arr) <= 1:
        return [-1]
    else:
        smallest = arr[0]
        idx = 0
        for i in range(1, len(arr)):
            if smallest > arr[i]:
                smallest = arr[i]
                idx = i
    arr.pop(idx)
    return arr


# 다른 풀이
# min 을 생각하지 못했다.
def otherSol(arr):
    if len(arr) <= 1:
        return [-1]
    else:
        arr.remove(min(arr))

    return arr


# testcase1
arr = [4, 3, 2, 1]
print(solution(arr))
