# 올바른 괄호

# 나의 풀이
def solution(s):
    answer = False
    if s[0] == ')':
        return answer
    tmp = list()
    for i in s:
        if i == '(':
            tmp.append(i)
        else:
            if not len(tmp):
                return answer
            else:
                tmp.pop()
    if len(tmp):  # 밑 3줄을 return len(tmp) == 0로 표현할 수 도 있다는 것을 발견
        return answer
    return True


# 다른 풀이
def otherSol(s):
    x = 0
    for w in s:
        if x < 0:
            break
        x = x + 1 if w == '(' else x - 1 if w == ')' else x
    return x == 0


# testcase1
s = "())(()"
print(solution(s))
print(otherSol(s))