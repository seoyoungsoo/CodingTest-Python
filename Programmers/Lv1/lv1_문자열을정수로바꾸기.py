# 문자열을 정수로 바꾸기

def solution(s):
    first = s[0]

    if first.isdigit():
        return int(s)
    else:
        if first == '+':
            return int(s[1:])
        else:
            return int('-' + s[1:])


# 다른 풀이
def strToInt(str):
    a = int(str)
    return a


# testcase 1
s = "-12345"
print(solution(s))

# 다른 풀이 testcase 2
str = "-5678"
print(strToInt(str))