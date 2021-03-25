# 큰 수 만들기

# 그리디 문제
def solution(number, k):
    stack = []

    for i, num in enumerate(number):
        while len(stack) > 0 and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        if k == 0:
            stack += list(number[i:])
            break
        stack.append(num)
    stack = stack[:-k] if k > 0 else stack

    return ''.join(stack)


# testcase1
number = "4177252841"
k = 4
print(solution(number, k))