# 짝지어 제거하기

# 나의 풀이
def solution(s):
    stack = []
    for i in s:
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    if stack:
        return 0
    else:
        return 1


# testcase1
s = 'baabaa'
print(solution(s))
