# 문자열 내림차순으로 배치하기

def solution(s):
    str = ""

    s_s = sorted(s, reverse=True)
    for i in s_s:
        str += i
    return str


# 다른 풀이
def sol(s):
    return ''.join(sorted(s, reverse=True))


# testcase 1
s = "Zbcdefg"
print(sol(s))
