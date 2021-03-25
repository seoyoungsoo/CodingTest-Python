# 문자열 내 p와 y의 개수

def solution(s):
    if s.lower().count('p') == s.lower().count('y'):
        return True
    else:
        return False


# testcase 1
s = "pPoooyY"
print(solution(s))
