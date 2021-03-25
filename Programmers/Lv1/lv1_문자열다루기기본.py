# 문자열 다루기 기본

def solution(s):
    if len(s) == 4 or len(s) == 6:
        try:
            if int(s):
                return True
        except:
            return False
    else:
        return False

# 다른 풀이
def sol(s):
    return s.isdigit() and len(s) in (4, 6)

# testcase 1
s = "a234"
print(solution(s))
