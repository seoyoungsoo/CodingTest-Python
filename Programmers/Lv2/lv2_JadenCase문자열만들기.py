# JadenCase 문자열 만들기

# 나의 풀이
def solution(s):
    result = ''
    tmp = ''

    for i in s:
        if not i == ' ':
            tmp += i
        else:
            result += tmp.capitalize() + i
            tmp = ''

    if len(tmp):
        result += tmp.capitalize()

    return result


# 다른 풀이
def otherSol(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])


# testcase1
s = "3people unFollowed me"
print(solution(s))
print(otherSol(s))
